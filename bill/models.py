from django.db import models, signals
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string
from customer.models import Customer
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone


class Bill(models.Model):
    bill_id = models.CharField('Bill ID',
                               max_length=6,
                               default=get_random_string(length=6, allowed_chars="ACY23456PKL#"))
    bill_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, db_index=True)
    billing_start_date = models.DateField()
    balance = models.FloatField(blank=True, null=True, default=0)
    total_bill = models.FloatField(blank=True, null=True)
    due_bill = models.BooleanField(default=True)
    total_due_bill = models.FloatField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Invoice(models.Model):
    invoice_id = models.CharField('Invoice ID',
                                  default=get_random_string(length=8, allowed_chars="FD23456PKL"),
                                  max_length=8,
                                  db_index=True)
    invoice_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)
    adjustment = models.FloatField(blank=True, null=True, default=0)
    is_paid = models.BooleanField(default=False)
    current_bill = models.FloatField('Current Bill', default=0)
    custom_bill_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)


@receiver(post_save, sender=Invoice)
def bill_balance_saved(sender, instance, created=False, **kwargs):
    if created:
        instance.bill.balance = instance.bill.balance + instance.current_bill
        instance.bill.save()


@receiver(post_save, sender=Invoice)
def adjustment_saved(sender, instance, created=True, **kwargs):
    if not created and instance.adjustment > 0:
        instance.bill.balance = instance.bill.balance - instance.adjustment
        instance.bill.save()
