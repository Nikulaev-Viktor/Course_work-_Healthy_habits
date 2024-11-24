from rest_framework import serializers

from habits.models import Habits
from habits.validators import RewardAndRelatedHabitValidator, DurationValidator, RelatedHabitValidator, \
    PleasantHabitValidator, FrequencyValidator


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'

    def validate(self, attrs):
        RewardAndRelatedHabitValidator()(attrs)
        DurationValidator()(attrs)
        RelatedHabitValidator()(attrs)
        PleasantHabitValidator()(attrs)
        FrequencyValidator()(attrs)
        return attrs


class HabitPublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habits
        fields = '__all__'
