from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.crypto import get_random_string

GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]




class Package(models.Model):
    package_name = models.CharField('Package', max_length=100, default='')
    package_bill = models.FloatField('Per Month Amount', default=0)
    month_cycle = models.IntegerField('Month Cycle', default=30)
    per_day_amount = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.package_name} - {self.package_bill}"

    @property
    def package_details(self):
        return f"{self.package_name} {self.month_cycle}"

    def save(self, *args, **kwargs):
        self.per_day_amount = "{:.2f}".format(self.package_bill / self.month_cycle)
        return super(Package, self).save(*args, **kwargs)


class Union(models.Model):
    union_name = models.CharField(max_length=100)
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
    customer_id = models.CharField('Customer ID',
                                   unique=True,
                                   max_length=6,
                                   default=str(get_random_string(length=6, allowed_chars='FDA1234567890'))
                                   )
    created_user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    name = models.CharField('Customer Name', max_length=200)
    package_name = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True)

    slug = models.SlugField(unique=True, blank=True, null=True)
    gender = models.CharField('Gender', choices=GENDER_CHOICES, default='M', max_length=1)
    phone_number = models.IntegerField(db_index=True, unique=True)
    email_field = models.EmailField(blank=True, null=True)
    alter_phone_number = models.IntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    total_due = models.FloatField(default=0)
    word_union = models.ForeignKey(Word, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"

    @property
    def customer_info(self):
        return f"{self.name} {self.phone_number}"

    @property
    def customer_word_union(self):
        return f"{self.word_union}"

    @property
    def customer_package_full(self):
        return f"{self.package_name}"

    @property
    def customer_create_date(self):
        return f"{self.created_at.date()}-{self.created_at.time()}"

    def get_absolute_url(self):
        return reverse('customer:customer_details', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        str_white_space_removed = self.name.replace(" ", "").lower()
        self.slug = f"{str_white_space_removed}-{self.customer_id.lower()}"
        super().save(*args, **kwargs)
