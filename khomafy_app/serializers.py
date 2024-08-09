from rest_framework import serializers
from .models import Song, Playlist


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ['id', 'title', 'artist', 'album', 'duration', 'release_date', 'song_url']


# class PlaylistSongSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Song
#         fields = ['title', 'artist', 'album', '']


class PlaylistSerializer(serializers.ModelSerializer):
    songs = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all(), many=True)

    class Meta:
        model = Playlist
        fields = ['id', 'name', 'description', 'songs']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['songs'] = SongSerializer(instance.songs.all(), many=True).data
        return representation
