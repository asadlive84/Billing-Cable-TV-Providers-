from bill.models import Bill
from customer.serializers import CustomerSerializer, BillSerializer
from customer.models import Customer
from rest_framework import generics


class CustomerListAPI(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerBillAPIView(generics.RetrieveAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
