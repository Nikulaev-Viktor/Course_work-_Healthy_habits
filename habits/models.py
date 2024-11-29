from datetime import timedelta
from django.core.exceptions import ValidationError
from django.conf import settings
from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    """"Модель привычек"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место',
                             help_text='место, в котором выполняется привычка', **NULLABLE)
    time = models.TimeField(verbose_name='время', help_text='время, когда выполняется привычка')

    action = models.CharField(max_length=100, verbose_name='действие',
                              help_text='действие, которое выполняется')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    related_habit = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.PositiveSmallIntegerField(default=1,
                                                 verbose_name='периодичность привычки, в днях',
                                                 help_text='укажите периодичность выполнения привычки в днях '
                                                           '(по умолчанию ежедневная)')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)
    complete_time = models.DurationField(verbose_name="Время на выполнение привычки", default=timedelta(seconds=120))
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    def __str__(self):
        return f'{self.user} будет выполнять {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'

    def clean(self):

        # Проверка RewardAndRelatedHabitValidator
        if self.reward and self.related_habit:
            raise ValidationError(
                'Нельзя указывать одновременно вознаграждение и связанную привычку. Выберите что-то одно.')

        # Проверка DurationValidator
        max_duration = timedelta(seconds=120)
        if self.complete_time and self.complete_time > max_duration:
            raise ValidationError(
                f"Время выполнения привычки не должно превышать {max_duration.total_seconds()} секунд.")

        # Проверка RelatedHabitValidator
        if self.related_habit and not self.related_habit.is_pleasant:
            raise ValidationError('Связанная привычка должна быть приятной.')

        # Проверка PleasantHabitValidator
        if self.is_pleasant:
            if self.reward:
                raise ValidationError('У приятной привычки не может быть вознаграждения.')
            if self.related_habit:
                raise ValidationError('У приятной привычки не может быть связанной привычки.')

        # Проверка FrequencyValidator
        if self.frequency and self.frequency > 7:
            raise ValidationError('Нельзя выполнять привычку реже, чем 1 раз в 7 дней.')

        super().clean()
