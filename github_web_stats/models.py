from django.db import models
from allauth.account.models import EmailAddress as AllauthEmailAddress
from django.contrib.auth.models import AbstractUser, PermissionsMixin, make_password

class User( AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, default=make_password('password'))

    class Meta:
        app_label = 'github_web_stats'
        verbose_name = 'user'
        verbose_name_plural = 'users'

class CustomEmailAddress(AllauthEmailAddress):
    pass

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    skills = models.CharField(max_length=255)
    customization_settings = models.JSONField(null=True)

    def __str__(self):
        return self.user.username

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()

class SocialIntegration(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    platform = models.CharField(max_length=50)
    profile_url = models.URLField()

class GitHubIntegration(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    github_name = models.EmailField(blank=True, null=True)  # Add this field
    repo_link = models.URLField()

    def __str__(self):
        return f"GitHubIntegration for {self.user.username}"

class Repository(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    url = models.URLField()

class CommitActivity(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    week = models.DateField()
    commits = models.IntegerField()

class CodeFrequency(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    week = models.DateField()
    additions = models.IntegerField()
    deletions = models.IntegerField()

class Participation(models.Model):
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    week = models.DateField()
    all_commits = models.IntegerField()
    owner_commits = models.IntegerField()