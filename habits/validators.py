from rest_framework.exceptions import ValidationError
from datetime import timedelta


class RewardAndRelatedHabitValidator:
    """ Валидатор для проверки одновременного заполнения полей `вознаграждение` и `связанная привычка`. """

    def __call__(self, attrs):
        if attrs.get('reward') and attrs.get('related_habit'):
            raise ValidationError(
                'Нельзя указывать одновременно вознаграждение и связанную привычку. Выберите что-то одно.'
            )


class DurationValidator:
    """ Валидатор для проверки времени выполнения привычки (не более 120 секунд). """

    def __init__(self, max_duration=timedelta(seconds=120)):
        self.max_duration = max_duration

    def __call__(self, attrs):
        complete_time = attrs.get('complete_time')

        if complete_time and complete_time > self.max_duration:
            raise ValidationError(
                f"Время выполнения привычки не должно превышать {self.max_duration.total_seconds()} секунд."
            )


class RelatedHabitValidator:
    """ Валидатор для проверки, что связанная привычка является приятной. """

    def __call__(self, attrs):
        related_habit = attrs.get('related_habit')
        if related_habit and not related_habit.is_pleasant:
            raise ValidationError(
                'Связанная привычка должна быть приятной.'
            )


class PleasantHabitValidator:
    """ Валидатор для проверки, что у приятной привычки нет ни вознаграждения, ни связанной привычки. """

    def __call__(self, attrs):
        if attrs.get('is_pleasant'):
            if attrs.get('reward'):
                raise ValidationError(
                    'У приятной привычки не может быть вознаграждения.'
                )
            if attrs.get('related_habit'):
                raise ValidationError(
                    'У приятной привычки не может быть связанной привычки.'
                )


class FrequencyValidator:
    """ Валидатор для проверки, что привычка выполняется не реже 1 раза в 7 дней. """

    def __call__(self, attrs):
        frequency = attrs.get('frequency')
        if frequency and frequency > 7:
            raise ValidationError(
                'Нельзя выполнять привычку реже, чем 1 раз в 7 дней.'
            )
