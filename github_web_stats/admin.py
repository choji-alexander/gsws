from django.contrib import admin
from allauth.account.admin import EmailAddressAdmin as AllauthEmailAddressAdmin
from django.contrib.auth.admin import UserAdmin
from django import forms
from allauth.account.models import EmailAddress as AllauthEmailAddress
from .models import User, Profile, Project, SocialIntegration, GitHubIntegration, CustomEmailAddress

class CustomUserAdmin(UserAdmin):
    # Define the fields to be displayed on the admin page
    list_display = ('username', 'email', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    search_fields = ('username', 'email')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions')

class EmailAddressForm(forms.ModelForm):
    class Meta:
        model = AllauthEmailAddress
        fields = ('email',)

class EmailAddressAdmin(AllauthEmailAddressAdmin):
    form = EmailAddressForm

admin.site.register(User, CustomUserAdmin)
admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(SocialIntegration)
admin.site.register(GitHubIntegration)
admin.site.unregister(AllauthEmailAddress)
admin.site.register(AllauthEmailAddress, EmailAddressAdmin)
