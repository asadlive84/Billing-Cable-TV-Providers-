from customer.models import Customer, Package, Union, Word
from bill.models import Invoice, Bill
from django import forms
from django.forms import ModelForm


class BillCheckingFrom(forms.Form):
    phone_num_customer_id = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'placeholder': 'Your mobile number or customer id'}))

    def __init__(self, *args, **kwargs):
        super(BillCheckingFrom, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control form-control-lg'


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
    custom_bill_date = forms.DateField()

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


class CreatePackageForm(forms.ModelForm):
    class Meta:
        model = Package
        fields = [
            'package_name',
            'package_bill',
            'month_cycle',
            'per_day_amount',
        ]

    def __init__(self, *args, **kwargs):
        super(CreatePackageForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CreateUnionForm(forms.ModelForm):
    class Meta:
        model = Union
        fields = [
            'union_name',
            'union_number',
            'help_info',
        ]

    def __init__(self, *args, **kwargs):
        super(CreateUnionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CreateWordForm(forms.ModelForm):
    class Meta:
        model = Word
        fields = [
            'union',
            'word_name',
            'word_number',
        ]

    def __init__(self, *args, **kwargs):
        super(CreateWordForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class CreateBillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = [
            'billing_start_date',
        ]

    def __init__(self, *args, **kwargs):
        super(CreateBillForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
