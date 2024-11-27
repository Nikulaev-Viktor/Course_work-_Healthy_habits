from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginations import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitSerializer, HabitPublicSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    """Эндпоинт для создания привычки"""
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitsListAPIView(generics.ListAPIView):
    """Эндпоинт для просмотра списка привычек"""
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class HabitsDetailAPIView(generics.RetrieveAPIView):
    """Эндпоинт для просмотра привычки"""
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    """Эндпоинт для обновления привычки"""
    queryset = Habits.objects.all()
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    """Эндпоинт для удаления привычки"""
    queryset = Habits.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsPublicListAPIView(generics.ListAPIView):
    """Эндпоинт для просмотра списка публичных привычек"""
    queryset = Habits.objects.all()
    serializer_class = HabitPublicSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)

