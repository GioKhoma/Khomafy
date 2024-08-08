from django.db import models


class Song(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    duration = models.DurationField()
    release_date = models.DateField()
    song_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title


class Playlist(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    songs = models.ManyToManyField(Song, related_name='playlists', blank=True)

    def __str__(self):
        return self.name

