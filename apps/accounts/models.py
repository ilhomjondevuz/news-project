from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    class Roles(models.TextChoices):
        Ordinary = 'O', 'ordinary',
        Admin = 'A', 'admin',
        Manager = 'M', 'manager',

    class Gender(models.TextChoices):
        Male = 'M', 'male',
        Female = 'F', 'female',

    role = models.CharField(max_length=1, choices=Roles.choices, default=Roles.Ordinary)
    gender = models.CharField(max_length=1, choices=Gender.choices, null=True, blank=True)
    birthDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User '
        verbose_name_plural = 'Users'
        ordering = ('username',)