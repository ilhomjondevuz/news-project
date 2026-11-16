from django.contrib.auth.models import AbstractUser
from django.db import models


class Account(AbstractUser):
    birthdate = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'accounts'
        ordering = ['-date_joined']
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'