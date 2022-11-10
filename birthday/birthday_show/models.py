from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime, date


class User(AbstractUser):
    """Модель пользователей."""
    
    dob = models.DateField(
        'date of birthday',
        auto_now_add=False,
        blank=False,
        null=True,
    )

    bio = models.TextField(
        'biography',
        blank=True,
    )

    username = models.CharField(
        'username',
        max_length=150,
        unique=True,
        blank=False,
        null=False
    )
    email = models.EmailField(
        'email',
        max_length=254,
        unique=True,
        blank=False,
        null=False
    )

    confirmation_code = models.CharField(
        'confirmation_code',
        max_length=70,
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        ordering = ['username']
        verbose_name = 'user'
        verbose_name_plural = 'users'


