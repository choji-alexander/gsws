# Generated by Django 4.2.13 on 2024-07-05 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_web_stats', '0010_rename_repo_url_githubintegration_repo_link_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='githubintegration',
            old_name='github_email',
            new_name='github_name',
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$KRq2n5MJ2L2TJqvU7oQNGS$CPlYZY1/E/aRx7C894PjvjqyoE8Y9HpgoZQCrt93AsM=', max_length=128),
        ),
    ]