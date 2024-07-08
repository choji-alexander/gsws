# Generated by Django 4.2.13 on 2024-07-05 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('github_web_stats', '0009_alter_user_password'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubintegration',
            old_name='repo_url',
            new_name='repo_link',
        ),
        migrations.RemoveField(
            model_name='githubintegration',
            name='repo_name',
        ),
        migrations.AddField(
            model_name='githubintegration',
            name='github_email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='githubintegration',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$fdEkTUvjxfLSu0Ilo4UTfp$lVYpVAIOvw169F9KbPz19CdGQf3JwkHOriqzsEzDeiw=', max_length=128),
        ),
    ]