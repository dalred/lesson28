# Generated by Django 4.0.1 on 2022-05-16 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.CharField(default='Unknown', max_length=20),
        ),
    ]