from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.utils.datetime_safe import datetime
from datetime import datetime
from customer.models import Customer
from bill.models import Bill, Invoice
from customer.forms import \
    CreateCustomerForm, \
    CreateInvoiceForm, \
    CreatePackageForm, \
    CreateUnionForm, \
    CreateWordForm, \
    CreateBillForm


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
        if forms.is_valid():
            customers = forms.save(commit=False)
            customers.created_user = request.user
            customers.save()
            messages.success(request, 'Customer Profile has been created successfully.')
            return HttpResponseRedirect(reverse('customer:customer_list'))
        else:
            messages.warning(request, 'Sorry, profile didn\'t create, duplicate mobile number isn\'t allowed')

    else:
        forms = CreateCustomerForm()

    return render(request, 'customers-template/create_customer.html', {'forms': forms, })


@login_required()
def edit_customer(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    forms = CreateCustomerForm(instance=customer)
    print(forms)
    return render(request, 'customers-template/customer_edit.html', {'customer': customer})


@login_required()
def create_invoices(request, customer_id):
    customer = Customer.objects.get(customer_id=customer_id)
    bill = Bill.objects.get(customer=customer.id)
    form = CreateInvoiceForm()

    if request.method == 'POST':
        form = CreateInvoiceForm(request.POST, request.FILES)
        custom_bill_date = request.POST.get('custom_bill_date')

        if form.is_valid():
            py_convert_date = datetime.strptime(custom_bill_date, "%d/%m/%Y")
            data = form.save(commit=False)
            data.bill = bill
            data.invoice_creator = request.user
            data.custom_bill_date = py_convert_date.date()
            data.save()
            x = Invoice.objects.get(pk=data.pk)
            print(x)
            messages.success(request, f"Success, You created invoice {data}")
            return HttpResponseRedirect(reverse('customer:customer_details', args=(customer.slug,)))
        else:
            messages.warning(request, "Invoice didn't create")
    else:
        form = CreateInvoiceForm()

    return render(request, 'customers-template/create_invoice.html', {'form': form, 'customer': customer})


@login_required()
def create_package(request):
    form = CreatePackageForm()
    if request.method == 'POST':
        form = CreatePackageForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            messages.success(request, "You created successfully your customer package!")
        else:
            messages.warning(request, "Failed!!")

    else:
        form = CreatePackageForm()

    return render(request, 'customers-template/create_package.html', {'form': form})


def create_union(request):
    form = CreateUnionForm()
    if request.method == 'POST':
        form = CreateUnionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!!")

        else:
            messages.warning(request, "Failed")
    return render(request, 'customers-template/create_union.html', {'form': form})


def create_word(request):
    form = CreateWordForm()
    if request.method == 'POST':
        form = CreateWordForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!!")

        else:
            messages.warning(request, "Failed")
    return render(request, 'customers-template/create_word.html', {'form': form})


def create_bill(request):
    form = CreateBillForm()
    if request.method == 'POST':
        form = CreateBillForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Success!!")

        else:
            messages.warning(request, "Failed")
    return render(request, 'customers-template/create_bill.html', {'form': form})
