from django.urls import path, include
from .views import RegisterAPIView, LoginAPIView, CurrentUserView, LogoutAPIView, ProfilesView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('profiles/', ProfilesView.as_view(), name='profiles'),
    # path(r'password-reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
    path('api-token-auth/', obtain_auth_token),
]