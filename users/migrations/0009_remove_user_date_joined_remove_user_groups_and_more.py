# Generated by Django 4.0.1 on 2022-05-16 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]