from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField(unique=True, default='01711123456')
    USERNAME_FIELD = 'phone_number'
    objects = CustomUserManager()



