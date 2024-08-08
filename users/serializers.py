from rest_framework import serializers
from .models import User
from rest_framework.exceptions import ValidationError
from rest_framework.authtoken.models import Token
from rest_framework import status


class UserLoginSerializer(serializers.ModelSerializer):
    id = serializers.PrimaryKeyRelatedField(read_only=True)
    email = serializers.EmailField(read_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'password']


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'first_name', 'last_name', 'password', 'password2']

    def validate_username(self, email):
        if User.objects.filter(email=email).exists():
            raise ValidationError('Email already registered')
        return email

    def validate(self, instance):
        if instance['password'] != instance['password2']:
            raise ValidationError({'message': 'Both password must match'})
        return instance

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email']


# class ResetPasswordRequestSerializer(serializers.Serializer):
#     email = serializers.EmailField(required=True)



