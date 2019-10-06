from customer.models import Customer
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
                  'word_union',]

    def __init__(self, *args, **kwargs):
        super(CreateCustomerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
