from django import template
from django.db.models import Sum
import re
from bill.models import Invoice

register = template.Library()


@register.filter()
def total_taka_users(user):
    pattern = "\d"
    invoice = Invoice.objects.filter(invoice_creator=user)
    total_taka = invoice.aggregate(amount=Sum('invoice_amount'))
    return total_taka['amount']
