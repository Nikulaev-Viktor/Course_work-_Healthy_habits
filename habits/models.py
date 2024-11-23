from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habits(models.Model):
    """"Модель привычек"""
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, verbose_name='создатель привычки', **NULLABLE)
    place = models.CharField(max_length=100, verbose_name='место',
                             help_text='место, в котором выполняется привычка')
    time = models.TimeField(verbose_name='время', help_text='время, когда выполняется привычка')
    action = models.CharField(max_length=100, verbose_name='действие',
                              help_text='действие, которое выполняется')
    is_pleasant = models.BooleanField(default=False, verbose_name='приятная привычка')
    sign_of_pleasant_habit = models.BooleanField(default=False, verbose_name='признак приятной привычки')
    related_habits = models.ForeignKey('self', on_delete=models.SET_NULL, verbose_name='связанная привычка', **NULLABLE)
    frequency = models.PositiveSmallIntegerField(default=1,
                                                 verbose_name='периодичность привычки, в днях')
    reward = models.CharField(max_length=255, verbose_name='вознаграждение', **NULLABLE)
    complete_time = models.DurationField(verbose_name="Время на выполнение привычки")
    is_public = models.BooleanField(default=False, verbose_name="Публичная привычка")

    def __str__(self):
        return self.action

    class Meta:
        verbose_name = 'привычка'
        verbose_name_plural = 'привычки'



