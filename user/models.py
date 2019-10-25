from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from bill.models import Invoice

PANEL_TYPES = (
    ('1', 'Admin'),
    ('2', 'Manager'),
    ('3', 'Worker'),
    ('4', 'Guest'),
)


class CustomUserManager(UserManager):
    pass


class CustomUser(AbstractUser):
    phone_number = models.PositiveIntegerField(unique=True)
    full_name = models.CharField(max_length=100)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=False)
    user_type = models.CharField(max_length=1, choices=PANEL_TYPES, default='4')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['full_name', ]
    objects = CustomUserManager()

    def __str__(self):
        return f'{self.full_name} - {self.phone_number}'


class CustomUserPermission(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
