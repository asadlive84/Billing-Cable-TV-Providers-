from customer.models import Customer
from bill.models import Invoice
from django import forms
from django.forms import ModelForm


class CreateCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name',
                  'package_name',
                  'customer_status',
                  'gender',
                  'phone_number',
                  'email_field',
                  'alter_phone_number',
                  'address',
                  'word_union', ]

    def __init__(self, *args, **kwargs):
        super(CreateCustomerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CreateInvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
            'invoice_type',
            'invoice_amount',
            'adjustment',
            'custom_bill_date',
        ]

    def __init__(self, *args, **kwargs):
        super(CreateInvoiceForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
