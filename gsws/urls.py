"""
URL configuration for gsws project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from github_web_stats.views import home, RepoActivityView, HistoricalDataViewSet, CustomAuthToken, github_callback, GithubCallbackView, LogoutView, get_github_data, link_social_profile, UserViewSet, ProfileViewSet, ProjectViewSet, SocialIntegrationViewSet, GitHubIntegrationViewSet, test_endpoint

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'profiles', ProfileViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'social-integrations', SocialIntegrationViewSet)
router.register(r'github-integrations', GitHubIntegrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('oauth/callback/', github_callback, name='github_callback'),
    path('api/', include(router.urls)),
    path('api/profiles/user/<int:user_id>/', ProfileViewSet.as_view({'get': 'retrieve'}), name='user-profile'),
    path('api/users/<int:user_id>/github_data/', get_github_data, name='get_github_data'),
    path('api/users/<int:user_id>/link_social_profile/', link_social_profile, name='link_social_profile'),
    path('home/<int:user_id>/', home, name='home'),
    path('api/profiles/${userId}/historical_data/>/', HistoricalDataViewSet.as_view, name='historical-data'),
    path('login/', CustomAuthToken.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/github/<str:username>/repos/<str:repoName>/activity', RepoActivityView.as_view(), name='repo-activity'),
]
