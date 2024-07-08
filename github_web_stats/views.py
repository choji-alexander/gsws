import requests
import logging
from django.shortcuts import redirect, render, get_object_or_404
from django.conf import settings
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets
from rest_framework.response import Response
from .models import User, Profile, Project, SocialIntegration, GitHubIntegration, Repository, CommitActivity, CodeFrequency, Participation
from .serializers import UserSerializer, ProfileSerializer, ProjectSerializer, SocialIntegrationSerializer, GitHubIntegrationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        if user_id:
            return self.queryset.filter(user__id=user_id)
        return self.queryset

    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id')
        if user_id:
            queryset = self.get_queryset()
            profile = get_object_or_404(queryset, user__id=user_id)
            serializer = self.get_serializer(profile)
            return Response(serializer.data)
        return super().retrieve(request, *args, **kwargs)

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SocialIntegrationViewSet(viewsets.ModelViewSet):
    queryset = SocialIntegration.objects.all()
    serializer_class = SocialIntegrationSerializer

class GitHubIntegrationViewSet(viewsets.ModelViewSet):
    queryset = GitHubIntegration.objects.all()
    serializer_class = GitHubIntegrationSerializer

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Assuming you are using JWT tokens
        try:
            request.user.auth_token.delete()
        except (AttributeError,):
            pass  # Token does not exist or already deleted
        
        return Response({"detail": "Logged out successfully."}, status=status.HTTP_200_OK)

class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        return Response({
            'token': token.key,
            'user_id': token.user_id,
            'username': user.username,
            'email': user.email
        })
     
class GithubCallbackView(APIView):
    def get(self, request):
        code = request.GET.get('code')
        token_url = "https://github.com/login/oauth/access_token"
        params = {
            "client_id": settings.GITHUB_CLIENT_ID,
            "client_secret": settings.GITHUB_CLIENT_SECRET,
            "code": code,
            "redirect_uri": "http://localhost:8000/oauth/callback",
        }
        headers = {'Accept': 'application/json'}
        response = requests.post(token_url, data=params, headers=headers)
        token = response.json().get('access_token')

        if not token:
            return JsonResponse({"error": "Failed to obtain token from GitHub"}, status=400)

        # Now you can use the token to make authenticated requests to GitHub's API
        user_data = requests.get(
            "https://api.github.com/user",
            headers={'Authorization': f'token {token}'}
        ).json()

        # Store user data and token in the session or database as needed
        request.session['user_data'] = user_data
        request.session['token'] = token

        return redirect(f'/home/{user_data["id"]}')  # Redirect to the home page or dashboard
    
class RepoActivityView(APIView):
    def get(self, request, username, repoName):
        logging.info(f"Fetching activity for repo {repoName} by user {username}")
        url = f'https://api.github.com/repos/{username}/{repoName}/stats/commit_activity'
        response = requests.get(url)
        if response.status_code == 200:
            return Response(response.json(), status=status.HTTP_200_OK)
        return Response({'detail': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

class HistoricalDataViewSet(viewsets.ViewSet):
    def retrieve(self, request, userId):
        profile = Profile.objects.get(user_id=userId)
        repositories = Repository.objects.filter(user=profile.user)
        commit_activity = CommitActivity.objects.filter(repository__in=repositories)
        code_frequency = CodeFrequency.objects.filter(repository__in=repositories)
        participation = Participation.objects.filter(repository__in=repositories)

        data = {
            'commit_activity': commit_activity.values('week', 'commits'),
            'code_frequency': code_frequency.values('week', 'additions', 'deletions'),
            'participation': participation.values('week', 'all_commits', 'owner_commits'),
        }
        return Response(data)
    
    
# GitHub Integration View
@api_view(['GET'])
def get_github_data(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Determine what data to fetch based on query parameters or nested routes
    data_type = request.query_params.get('type', None)
    
    if data_type == 'repos':
        # Fetch GitHub repositories
        response = requests.get(f'https://api.github.com/users/{user.username}/repos')
        if response.status_code != 200:
            return Response({'detail': 'Error fetching GitHub repositories'}, status=status.HTTP_400_BAD_REQUEST)
        
        repos_data = response.json()
        return Response(repos_data, status=status.HTTP_200_OK)
    
    elif data_type == 'userinfo':
        # Fetch GitHub user information
        response = requests.get(f'https://api.github.com/users/{user.username}')
        if response.status_code != 200:
            return Response({'detail': 'Error fetching GitHub user information'}, status=status.HTTP_400_BAD_REQUEST)
        
        userinfo_data = response.json()
        return Response(userinfo_data, status=status.HTTP_200_OK)
    
    elif data_type == 'events':
        # Fetch GitHub events
        response = requests.get(f'https://api.github.com/users/{user.username}/events')
        if response.status_code != 200:
            return Response({'detail': 'Error fetching GitHub events'}, status=status.HTTP_400_BAD_REQUEST)
        
        events_data = response.json()
        return Response(events_data, status=status.HTTP_200_OK)
    
    else:
        return Response({'detail': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

# Social Integration View
@api_view(['POST'])
def link_social_profile(request, user_id):
    user = User.objects.get(id=user_id)
    platform = request.data['platform']
    profile_url = request.data['profile_url']
    social_integration = SocialIntegration.objects.create(user=user, platform=platform, profile_url=profile_url)
    return Response({'status': 'Profile linked successfully!'})

@api_view(['GET'])
def test_endpoint(request):
    return Response({'message': 'Hello from the backend!'})

@api_view(['POST'])
def create_user(request):
    print(request.data)  # Add this line to print the request data
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        Profile.objects.create(user=serializer)
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

def github_login(request):
    github_auth_url = "https://github.com/login/oauth/authorize"
    params = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "redirect_uri": "http://localhost:8000/oauth/callback",
        "scope": "read:user repo",
    }
    url = f"{github_auth_url}?{requests.compat.urlencode(params)}"
    return redirect(url)

def github_callback(request):
    code = request.GET.get('code')
    token_url = "https://github.com/login/oauth/access_token"
    params = {
        "client_id": settings.GITHUB_CLIENT_ID,
        "client_secret": settings.GITHUB_CLIENT_SECRET,
        "code": code,
        "redirect_uri": "http://localhost:8000/oauth/callback",
    }
    headers = {'Accept': 'application/json'}
    response = requests.post(token_url, data=params, headers=headers)
    token = response.json().get('access_token')

    # Fetch user data from GitHub
    user_data = requests.get(
        "https://api.github.com/user",
        headers={'Authorization': f'token {token}'}
    ).json()

    # Check if the user exists in the database, if not, create a new user
    github_username = user_data.get('login')
    user, created = User.objects.get_or_create(username=github_username)
    if created:
        user.github_username = github_username
        user.save()

    # Generate a token for the user
    token, _ = Token.objects.get_or_create(user=user)

    # Redirect to the React frontend with the user ID and token
    return redirect(f'http://localhost:3000/home/{user.id}?token={token.key}')  # Redirect to the home page or dashboard

def home(request, user_id):
    context = {
        'user_id': user_id
    }
    return redirect(f'http://127.0.0.1:3000/home/{user_id}') 
