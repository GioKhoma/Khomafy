# Generated by Django 5.1 on 2024-08-08 19:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_passwordreset'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PasswordReset',
        ),
    ]
