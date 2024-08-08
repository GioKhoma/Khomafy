from rest_framework import generics
from .models import Song, Playlist
from .serializers import SongSerializer, PlaylistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class SongListView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class SongDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PlaylistListView(generics.ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [IsAuthenticated]
