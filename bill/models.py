from django.db import models, signals
from django.db.models.signals import post_save, pre_save
from django.utils.crypto import get_random_string
from customer.models import Customer
from django.conf import settings
from django.dispatch import receiver
from django.utils import timezone
from datetime import datetime, timedelta

ACTIVE = '1'
INACTIVE = '0'

BILL_STATUS = [
    (INACTIVE, 'Inactive'),
    (ACTIVE, 'Active'),
]

DUE_BILL = '0'
NEW_CONNECTION = '1'
CURRENT_BILL = '2'
ADVANCE_BILL = '3'

INVOICE_TYPE = [
    (DUE_BILL, 'Due Bill'),
    (NEW_CONNECTION, 'New Connection'),
    (CURRENT_BILL, 'Current Bill'),
    (ADVANCE_BILL, 'Advance Bill'),
]


class BillHistory(models.Model):
    date_version = models.IntegerField(editable=False)
    bill = models.ForeignKey('Bill', on_delete=models.CASCADE)
    connection_date_new = models.DateField()
    connection_date_end = models.DateField(blank=True, null=True)
    user_new_bill = models.FloatField(default=0, blank=True)
    total_days = models.FloatField(blank=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('date_version', 'bill')

    def __str__(self):
        return f"{self.bill.customer.name} {self.date_version} | {self.connection_date_new}"

    @property
    def last_activate_date(self):
        return self.connection_date_new

    def save(self, *args, **kwargs):
        # start with version 1 and increment it for each bill

        if self.bill.connection_date_end:
            self.connection_date_end = self.bill.connection_date_end

        current_date_version = BillHistory.objects.filter(bill=self.bill).order_by('-date_version')[:1]
        self.date_version = current_date_version[0].date_version + 1 if current_date_version else 1
        # days and bill calculate from new connection date
        if self.connection_date_end:
            self.total_days = round((self.connection_date_end - self.connection_date_new).days, 1)
        else:
            self.total_days = round((timezone.now().date() - self.connection_date_new).days, 1)

        self.user_new_bill = round(
            sum([i.bill.customer.package_name.per_day_amount for i in current_date_version]) * self.total_days, 2)

        super(BillHistory, self).save(*args, **kwargs)


class Bill(models.Model):
    bill_id = models.CharField('Bill ID',
                               unique=True,
                               max_length=6,
                               default=get_random_string(length=6, allowed_chars="ACY23456PKLW"))
    bill_creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    customer = models.OneToOneField(Customer, on_delete=models.SET_NULL, null=True, db_index=True)
    billing_start_date = models.DateField(blank=True)
    connection_date_end = models.DateField(blank=True, null=True)
    bill_status = models.CharField(choices=BILL_STATUS, default=ACTIVE, max_length=1)
    balance = models.FloatField(default=0)
    due_bill_status = models.BooleanField('Due Status', default=True)
    due_bill = models.FloatField(default=0, blank=True)
    user_has_bill = models.FloatField(default=0, blank=0)
    # connection bill if object has new connection bill
    connection_bill = models.FloatField(null=0, blank=0, default=0)
    # bill paid user
    user_bill_paid = models.FloatField(blank=0, default=0)
    total_day = models.IntegerField(blank=True, null=True)
    last_total_day_for_new_date = models.IntegerField(blank=True, null=True)
    last_user_has_bill = models.FloatField(default=0, blank=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.name}"

    def bill_history(self):
        return BillHistory.objects.filter(bill=self).order_by('-date_version')

    def days_history(self):
        b = BillHistory.objects.filter(bill=self).order_by('-date_version')[:1]
        return sum([x.total_days for x in b])

    def last_user_bill(self):
        b = BillHistory.objects.filter(bill=self).order_by('-date_version')[:1]
        return sum([x.user_new_bill for x in b])

    def save(self, *args, **kwargs):
        self.balance = self.connection_bill + self.user_bill_paid
        if not self.billing_start_date:
            self.billing_start_date = timezone.now().date()

        if self.bill_status == '0':
            self.connection_date_end = timezone.now().date()
            self.total_day = (self.connection_date_end - self.billing_start_date).days
        else:
            self.connection_date_end = None
            self.total_day = (timezone.now().date() - self.billing_start_date).days

        self.last_total_day_for_new_date = self.days_history()
        self.last_user_has_bill = self.last_user_bill()
        self.user_has_bill = round(
            (timezone.now().date() - self.billing_start_date).days * self.customer.package_name.per_day_amount, 2)
        self.due_bill = round(self.user_bill_paid - self.user_has_bill, 2)
        if self.user_bill_paid >= self.user_has_bill:
            self.due_bill_status = False
        elif self.user_bill_paid < self.user_has_bill:
            self.due_bill_status = True

        super().save(*args, **kwargs)

        bill_history = self.bill_history()
        if not bill_history or self.billing_start_date != bill_history[0].connection_date_new or self.connection_date_end:
            new_bill_date_history = BillHistory(bill=self,
                                                connection_date_new=self.billing_start_date,
                                                connection_date_end=self.connection_date_end
                                                )

            print(f"Hello Dear {new_bill_date_history.connection_date_end}")
            new_bill_date_history.save()


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
    comment = models.CharField(max_length=200, blank=True, null=True)
    custom_bill_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.invoice_amount}"

    def save(self, *args, **kwargs):
        self.invoice_id = str(get_random_string(length=8, allowed_chars="FD23456PKL"))

        super().save(*args, **kwargs)

    class Meta:
        ordering = ('-custom_bill_date',)


@receiver(post_save, sender=Invoice)
def bill_balance_saved(sender, instance, created=False, **kwargs):
    if created:
        '''
        Amount saved Bill instance objects
        '''

        # user has new connection then bill amount saved connection_bill field
        # if instance.invoice_type == '1':
        #     instance.bill.connection_bill = instance.bill.connection_bill + instance.invoice_amount
        # else:
        #     # all bill amount will be saved invoice_bill_collector of bill model
        instance.bill.user_bill_paid = instance.bill.user_bill_paid + instance.invoice_amount

        instance.bill.save()

# @receiver(post_save, sender=Invoice)
# def adjustment_saved(sender, instance, created=True, **kwargs):
#     get_bill_start_date = instance.bill.billing_start_date
#     day = get_bill_start_date.today() - get_bill_start_date
#     if not created and instance.adjustment > 0:
#         '''
#         Amount adjustment saved Bill instance objects
#         total day count and saved for Customer (Bill instance objects)
#
#         '''
#         instance.bill.balance = instance.bill.balance - instance.adjustment
#         instance.bill.invoice_bill_collector = instance.bill.invoice_bill_collector - instance.invoice_amount
#         instance.bill.due_bill = round(instance.bill.total_bill - instance.bill.balance, 2)
#         instance.bill.save()
