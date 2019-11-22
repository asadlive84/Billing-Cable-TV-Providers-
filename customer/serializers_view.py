from bill.models import Bill
from customer.serializers import CustomerSerializer, BillSerializer
from customer.models import Customer
from rest_framework import generics, filters


class CustomerListAPI(generics.ListAPIView):
    search_fields = ['phone_number', 'customer_id']
    filter_backends = (filters.SearchFilter,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerBillAPIView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
