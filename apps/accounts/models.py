from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        Ordinary = 'O', 'ordinary',
        Admin = 'A', 'admin',
        Manager = 'M', 'manager',

    role = models.CharField(max_length=1, choices=Roles.choices, default=Roles.Ordinary)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User '
        verbose_name_plural = 'Users'
        ordering = ('username',)