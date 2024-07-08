from rest_framework import serializers
from allauth.account.models import EmailAddress
from .models import User, Profile, Project, SocialIntegration, GitHubIntegration

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
    
    def create(self, validated_data):
        print(validated_data)  # Add this line to print the validated data
        user = User.objects.create_user(
                    username=validated_data['username'],
                    email=validated_data['email'],
                    password=validated_data['password']
                )        
        user.save()
        # Create an EmailAddress instance for the user
        # email_address = EmailAddress.objects.create(
        #     user=user,
        #     email=user.email,
        #     verified=True,
        #     primary=True
        # )
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'skills', 'customization_settings']

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['user', 'title', 'description']

class SocialIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialIntegration
        fields = ['user', 'platform', 'profile_url']

class GitHubIntegrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubIntegration
        fields = ['user', 'repo_name', 'repo_url']
