from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from users.models import User
from users.permissions import IsSuperuser, IsOwner
from users.serializers import MyTokenObtainPairSerializer, UserSerializer


class MyTokenObtainPair(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """Эндпоинт регистрации пользователя"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    """Эндпоинт получения списка пользователей"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsSuperuser)


class UserDetailAPIView(generics.RetrieveAPIView):
    """Эндпоинт получения информации о пользователе"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwner | IsSuperuser)


class UserUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт изменения информации о пользователе"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwner)

    def perform_update(self, serializer):
        serializer.save()


class UserDelete(generics.DestroyAPIView):
    """Эндпоинт удаления пользователя"""
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated, IsOwner)
