from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Модель пользователей"""
    username = None

    first_name = models.CharField(
        max_length=100,
        verbose_name='имя')
    email = models.EmailField(
        unique=True,
        verbose_name='email',
        help_text='введите email')
    phone_number = models.CharField(
        max_length=35,
        verbose_name='номер телефона',
        **NULLABLE,
        help_text='введите номер телефона')
    avatar = models.ImageField(
        upload_to='users/avatars/',
        verbose_name='аватар', **NULLABLE,
        help_text='загрузите свой аватар')
    tg_nick = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        verbose_name="TG ник",
        help_text="Укажите свой ник",
    )
    tg_chat_id = models.CharField(
        max_length=50,
        verbose_name="ID чата",
        help_text="Укажите ID чата",
        **NULLABLE
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.first_name}, {self.email}, {self.tg_nick}'

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'
