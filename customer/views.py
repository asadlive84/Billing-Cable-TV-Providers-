from django.shortcuts import render, get_object_or_404
from customer.models import Customer


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customer/customer_list.html', {'customers': customers})


def customer_details(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    return render(request, 'customer/customer_details.html', {'customer': customer})
