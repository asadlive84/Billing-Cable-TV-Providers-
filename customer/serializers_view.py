from customer.serializers import CustomerSerializer
from customer.models import Customer
from rest_framework import generics


class CustomerListAPI(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
