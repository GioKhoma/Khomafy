from rest_framework.views import APIView
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.contrib.auth import authenticate
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import os


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginAPIView(APIView):
    def post(self, request, *args, **kargs):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            response = {
                "email": {
                    "detail": "User Does not exist!"
                }
            }
            if User.objects.filter(email=request.data['email']).exists():
                user = User.objects.get(email=request.data['email'])
                token, created = Token.objects.get_or_create(user=user)
                response = {
                    'success': True,
                    'email': user.email,
                    'token': token.key
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(response, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args):
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'success': True, 'detail': "Logged out successfully!"}, status=status.HTTP_200_OK)


class CurrentUserView(generics.RetrieveUpdateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


# class RequestPasswordReset(generics.GenericAPIView):
#     permission_classes = [AllowAny]
#     serializer_class = ResetPasswordRequestSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         email = request.data['email']
#         user = User.objects.filter(email__iexact=email).first()
#
#         if user:
#             token_generator = PasswordResetTokenGenerator()
#             token = token_generator.make_token(user)
#             reset = PasswordReset(email=email, token=token)
#             reset.save()
#
#             reset_url = f"{os.environ['PASSWORD_RESET_BASE_URL']}/{token}"
#
#             return Response({'success': 'We have sent you a link to reset your password!'}, status=status.HTTP_200_OK)
#         else:
#             return Response({'error': 'User with credentials not found.'}, status=status.HTTP_404_NOT_FOUND)


class ProfilesView(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()
