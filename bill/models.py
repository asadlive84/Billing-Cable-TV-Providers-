from django.db import models
from django.utils.crypto import get_random_string

from customer.models import Customer
from django.conf import settings


class Bill(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    billing_start_date = models.DateField()
    total_bill = models.FloatField()
    due_bill = models.BooleanField(default=True)
    total_due_bill = models.FloatField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Invoice(models.Model):
    invoice_id = models.CharField('Invoice ID', default=get_random_string(length=8, allowed_chars="FD23456PKL"), max_length=8, db_index=True)
    invoice_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    is_paid = models.BooleanField(default=False)
    current_bill = models.FloatField('Current Bill')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.invoice_id = get_random_string(length=6)
        super().save(*args, **kwargs)
