from bill.models import Bill, Invoice
from customer.models import Customer, Package, Union, Word
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['customer_id',
                  'created_user',
                  'name',
                  'package_name',
                  'phone_number',
                  'word_union',
                  'customer_create_date',
                  'customer_word_union',
                  'customer_package_full',
                  ]


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['invoice_creator', 'invoice_type', 'invoice_amount', 'custom_bill_date',]


class BillSerializer(serializers.ModelSerializer):

    invoice = InvoiceSerializer(many=True, read_only=True)

    class Meta:
        model = Bill
        fields = ['customer', 'billing_start_date', 'invoice']