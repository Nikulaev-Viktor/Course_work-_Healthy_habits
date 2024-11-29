from django.contrib import admin

from habits.models import Habits


@admin.register(Habits)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'place', 'time', 'action', 'is_pleasant', 'related_habit', 'frequency',
        'reward',
        'complete_time', 'is_public')
    list_filter = ('is_pleasant', 'is_public', 'frequency')
    search_fields = ('id', 'action', 'place')
