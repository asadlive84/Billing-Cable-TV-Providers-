from django.db import models, signals
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string
from customer.models import Customer
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone

DUE_BILL = '0'
NEW_CONNECTION = '1'
CURRENT_BILL = '2'

INVOICE_TYPE = [
    (DUE_BILL, 'Due Bill'),
    (NEW_CONNECTION, 'New Connection'),
    (CURRENT_BILL, 'Current Bill'),
]


class Bill(models.Model):
    bill_id = models.CharField('Bill ID',
                               unique=True,
                               max_length=6,
                               default=get_random_string(length=6, allowed_chars="ACY23456PKLW"))
    bill_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, db_index=True)
    billing_start_date = models.DateField()
    balance = models.FloatField(default=0)
    total_bill = models.FloatField('Total Bill', default=0)
    due_bill_status = models.BooleanField('Due Status', default=True)
    due_bill = models.FloatField('Due Bill', default=0)
    total_day = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Invoice(models.Model):
    invoice_id = models.CharField('Invoice ID',
                                  unique=True,
                                  blank=True,
                                  max_length=8,
                                  db_index=True)
    # invoice creator as sales person or bill collect
    invoice_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    # Bill person
    bill = models.ForeignKey(Bill, on_delete=models.SET_NULL, null=True)
    # invoice type
    invoice_type = models.CharField(choices=INVOICE_TYPE, max_length=1, default=CURRENT_BILL)
    # given amount
    invoice_amount = models.FloatField('Invoice Amount', default=0)
    adjustment = models.FloatField(blank=True, null=True, default=0)
    custom_bill_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.bill.customer.name} {self.invoice_amount} {self.invoice_creator}"

    def save(self, *args, **kwargs):
        self.invoice_id = str(get_random_string(length=8, allowed_chars="FD23456PKL"))
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-created_at',)


@receiver(post_save, sender=Invoice)
def bill_balance_saved(sender, instance, created=False, **kwargs):
    get_bill_start_date = instance.bill.billing_start_date
    day = get_bill_start_date.today() - get_bill_start_date
    if created:
        '''
        Amount saved Bill instance objects
        '''
        instance.bill.balance = instance.bill.balance + instance.invoice_amount

        '''
        total day count and saved for Customer(Bill instance objects)
        '''
        instance.bill.total_day = day.days
        instance.bill.total_bill = round(instance.bill.customer.package_name.per_day_amount * instance.bill.total_day, 2)
        instance.bill.due_bill = round(instance.bill.total_bill-instance.bill.balance, 2)
        instance.bill.save()
    if not created:
        instance.bill.total_day = day.days
        instance.bill.total_bill = round(instance.bill.customer.package_name.per_day_amount * instance.bill.total_day, 2)
        instance.bill.due_bill = round(instance.bill.total_bill - instance.bill.balance, 2)
        instance.bill.save()


@receiver(post_save, sender=Invoice)
def adjustment_saved(sender, instance, created=True, **kwargs):
    get_bill_start_date = instance.bill.billing_start_date
    day = get_bill_start_date.today() - get_bill_start_date
    if not created and instance.adjustment > 0:
        '''
        Amount adjustment saved Bill instance objects
        total day count and saved for Customer (Bill instance objects)
        
        '''
        instance.bill.balance = instance.bill.balance - instance.adjustment
        instance.bill.total_day = day.days
        instance.bill.total_bill = round(instance.bill.customer.package_name.per_day_amount * instance.bill.total_day, 2)
        instance.bill.due_bill = round(instance.bill.total_bill-instance.bill.balance, 2)
        instance.bill.save()
