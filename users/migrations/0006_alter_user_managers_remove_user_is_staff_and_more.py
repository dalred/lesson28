# Generated by Django 4.0.1 on 2022-05-16 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_age'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_superuser',
        ),
    ]