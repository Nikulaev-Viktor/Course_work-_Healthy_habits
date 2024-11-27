from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserDelete, UserListAPIView, UserDetailAPIView, UserUpdateAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('list/', UserListAPIView.as_view(), name='list'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', UserUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', UserDelete.as_view(), name='delete'),
]
