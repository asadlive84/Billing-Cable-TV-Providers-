from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from customer.models import Customer
from customer.forms import CreateCustomerForm


@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers-template/customer_list.html', {'customers': customers})


@login_required()
def customer_details(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    return render(request, 'customers-template/customer_details.html', {'customer': customer})


@login_required()
def create_customer(request):
    forms = CreateCustomerForm()

    if request.method == 'POST':
        forms = CreateCustomerForm(request.POST, request.FILES)
        customers = forms.save(commit=False)
        customers.created_user = request.user
        customers.save()
    else:
        forms = CreateCustomerForm()

    return render(request, 'customers-template/create_customer.html', {'forms': forms, })
