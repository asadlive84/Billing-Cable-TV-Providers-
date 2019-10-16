from customer.models import Customer, Package, Union, Word
from rest_framework import serializers


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['customer_id',
                  'created_user',
                  'name',
                  'package_name',
                  'customer_status',
                  'phone_number',
                  'word_union',
                  'customer_create_date',
                  'customer_word_union',
                  'customer_package_full',
                  ]