from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.username} - {self.phone_number}'


class User(models.Model):
    pass
