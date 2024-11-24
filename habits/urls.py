from django.urls import path

from habits.apps import HabitsConfig
from habits.views import (HabitsCreateAPIView, HabitsDestroyAPIView, HabitsListAPIView, HabitsPublicListAPIView,
                        HabitsRetrieveAPIView, HabitsUpdateAPIView)

app_name = HabitsConfig.name

urlpatterns = [
    path('create/', HabitsCreateAPIView.as_view(), name='create'),
    path('', HabitsListAPIView.as_view(), name='list'),
    path('<int:pk>/', HabitsRetrieveAPIView.as_view(), name='retrieve'),
    path('update/<int:pk>/', HabitsUpdateAPIView.as_view(), name='update'),
    path('delete/<int:pk>/', HabitsDestroyAPIView.as_view(), name='delete'),
    path('public/', HabitsPublicListAPIView.as_view(), name='public_list'),
  ]
