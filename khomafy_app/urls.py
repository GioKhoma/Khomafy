from django.urls import path
from .views import SongListView, SongDetailView, PlaylistListView

urlpatterns = [
    path('songs/', SongListView.as_view(), name='songs'),
    path('songs/<int:pk>/', SongDetailView.as_view(), name='song-detail'),
    path('playlists/', PlaylistListView.as_view(), name='playlists'),
]