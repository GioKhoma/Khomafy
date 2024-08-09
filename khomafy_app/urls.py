from django.urls import path
from .views import SongListView, SongDetailView, PlaylistListView, PlaylistDetailView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='songs'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlists'),
    path('playlists/<int:pk>/', PlaylistDetailView.as_view(), name='playlist-detail'),
]