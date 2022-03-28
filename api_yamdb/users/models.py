from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole:
    USER = 'user'
    MODERATOR = 'moderator'
    ADMIN = 'admin'


CHOICES_ROLE = (
    (UserRole.USER, 'user'),
    (UserRole.MODERATOR, 'moderator'),
    (UserRole.ADMIN, 'admin'),
)


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Имя пользователя',
        max_length=150,
        unique=True
    )
    email = models.EmailField(
        verbose_name='Почта',
        unique=True,
    )
    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
        blank=True
    )
    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
        blank=True
    )
    bio = models.TextField(
        verbose_name='Биография',
        null=True
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=16,
        choices=CHOICES_ROLE,
        default='user'
    )

    @property
    def is_admin(self):
        return self.role == UserRole.ADMIN

    @property
    def is_moderator(self):
        return self.role == UserRole.MODERATOR

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
