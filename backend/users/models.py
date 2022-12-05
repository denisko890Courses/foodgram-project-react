from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    username = models.CharField(
        max_length=150,
        unique=True,
        verbose_name='Никнейм пользователя (обязательно):'
    )
    password = models.CharField(
        max_length=150,
        blank=True,
        verbose_name='Пароль'
    )
    email = models.EmailField(
        max_length=150,
        unique=True,
        verbose_name='Адрес электронной почты (обязательно):'
    )
    first_name = models.CharField(
        max_length=150,
        unique=False,
        verbose_name='Имя'
    )
    second_name = models.CharField(
        max_length=150,
        unique=False,
        verbose_name='Фамилия'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'second_name', 'password']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
