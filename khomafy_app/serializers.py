from rest_framework import serializers
from .models import Song, Playlist


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'duration', 'release_date', 'song_url']


class PlaylistSerializer(serializers.ModelSerializer):
    songs = SongSerializer(many=True, read_only=True)

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'songs']