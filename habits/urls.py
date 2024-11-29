from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIView,
                          HabitsDestroyAPIView,
                          HabitsListAPIView,
                          HabitsPublicListAPIView,
                          HabitsDetailAPIView,
                          HabitsUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('', HabitsListAPIView.as_view(), name='list'),
    path('create/', HabitsCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', HabitsDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='delete'),
    path('public/', HabitsPublicListAPIView.as_view(), name='public_list'),
  ]
