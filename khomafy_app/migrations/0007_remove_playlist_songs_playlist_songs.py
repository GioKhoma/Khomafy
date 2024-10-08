# Generated by Django 5.1 on 2024-08-08 21:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('khomafy_app', '0006_rename_artist_playlist_name_remove_playlist_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='playlist',
            name='songs',
        ),
        migrations.AddField(
            model_name='playlist',
            name='songs',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='playlists', to='khomafy_app.song'),
            preserve_default=False,
        ),
    ]
