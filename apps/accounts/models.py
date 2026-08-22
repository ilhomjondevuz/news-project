from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    class Roles(models.TextChoices):
        Ordinary = 'O', 'ordinary',
        Admin = 'A', 'admin',
        Manager = 'M', 'manager',

    class Gender(models.TextChoices):
        Male = 'M', 'male',
        Female = 'F', 'female',

    email = models.EmailField(verbose_name=_("Email"), max_length=254, unique=True)
    role = models.CharField(max_length=1, choices=Roles.choices, default=Roles.Ordinary, verbose_name=_("Role"))
    gender = models.CharField(max_length=1, choices=Gender.choices, null=True, blank=True, verbose_name=_("Gender"))
    birthDate = models.DateField(null=True, blank=True, verbose_name=_("Birth Date"))

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = 'User '
        verbose_name_plural = 'Users'
        ordering = ('username',)