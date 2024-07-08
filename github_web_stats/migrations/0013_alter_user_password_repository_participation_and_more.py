# Generated by Django 4.2.13 on 2024-07-08 18:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('github_web_stats', '0012_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$WjPvQCjfPsIm9SUf6nOzZY$iZx1mc2dou7kV2VpM2EysZLhPxcek9qef0xtwPBbhjk=', max_length=128),
        ),
        migrations.CreateModel(
            name='Repository',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('url', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Participation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField()),
                ('all_commits', models.IntegerField()),
                ('owner_commits', models.IntegerField()),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github_web_stats.repository')),
            ],
        ),
        migrations.CreateModel(
            name='CommitActivity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField()),
                ('commits', models.IntegerField()),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github_web_stats.repository')),
            ],
        ),
        migrations.CreateModel(
            name='CodeFrequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week', models.DateField()),
                ('additions', models.IntegerField()),
                ('deletions', models.IntegerField()),
                ('repository', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='github_web_stats.repository')),
            ],
        ),
    ]