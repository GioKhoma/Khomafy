from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserView, LogoutAPIView, ProfilesView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('user/', UserView.as_view(), name='user'),
    path('profiles/', ProfilesView.as_view(), name='profiles'),
    path('api-token-auth/', obtain_auth_token),
]