from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habits
from habits.paginations import HabitPagination
from habits.permissions import IsOwner
from habits.serializers import HabitsSerializer, HabitPublicSerializer


class HabitsCreateAPIView(generics.CreateAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitsListAPIView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = HabitPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user=self.request.user)


class HabitsRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]


class HabitsUpdateAPIView(generics.UpdateAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitsSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class HabitsDestroyAPIView(generics.DestroyAPIView):
    serializer_class = HabitsSerializer
    permission_classes = [IsOwner]


class HabitsPublicListAPIView(generics.ListAPIView):
    queryset = Habits.objects.all()
    serializer_class = HabitPublicSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = HabitPagination

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(is_public=True)

