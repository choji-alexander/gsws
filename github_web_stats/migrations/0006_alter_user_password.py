# Generated by Django 4.2.13 on 2024-07-05 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('github_web_stats', '0005_customemailaddress_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$rk1SswMlwHNeZOBCp6JqrP$O273ZP4jvVfMNNjVNsJLc1oNoHiOqPaPsaECqaCoEJw=', max_length=128),
        ),
    ]
