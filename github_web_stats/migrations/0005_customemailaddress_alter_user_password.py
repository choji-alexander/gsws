# Generated by Django 4.2.13 on 2024-07-05 03:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_emailaddress_unique_primary_email'),
        ('github_web_stats', '0004_alter_user_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomEmailAddress',
            fields=[
                ('emailaddress_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='account.emailaddress')),
            ],
            bases=('account.emailaddress',),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$UNXr2HMHV6W8yXFwqVVprC$pvLX4IhCjIJzzGFY5Q5wvwGMDFlc+FRXc1HSoPehZZk=', max_length=128),
        ),
    ]
