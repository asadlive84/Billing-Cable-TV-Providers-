from django.db import models
from django.conf import settings
from django.utils.crypto import get_random_string

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
)


class Union(models.Model):
    union_name = models.CharField(max_length=100, default=True)
    union_number = models.IntegerField()
    help_info = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.union_name} - {self.union_number} "

    @property
    def union_info(self):
        return f"{self.union_name} - {self.union_number} "


class Word(models.Model):
    union = models.OneToOneField(Union, on_delete=models.SET_NULL, null=True)
    word_name = models.CharField(max_length=100)
    word_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.union.union_name} - {self.word_name} -{self.word_number}"

    @property
    def word_info(self):
        return f"{self.union.union_name} - {self.word_name} - {self.word_number}"


class Customer(models.Model):
    """
        Customer Data Table
    """
    customer_id = models.CharField('Customer ID', max_length=6)
    name = models.CharField('Customer Name', max_length=200, db_index=True)
    slug = models.SlugField(unique=True, blank=True, null=True)
    gender = models.CharField('Gender', choices=GENDER_CHOICES, default='M', max_length=1)
    phone_number = models.IntegerField(db_index=True)
    alter_phone_number = models.IntegerField()
    address = models.TextField()
    word_union = models.ForeignKey(Word, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    @property
    def customer_info(self):
        return f"{self.name} {self.phone_number}"

    def save(self):
        self.customer_id = get_random_string(length=6)


