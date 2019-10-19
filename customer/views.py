from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
# from django.utils.datetime_safe import datetime
from datetime import datetime, timedelta
from customer.models import Customer
from bill.models import Bill, Invoice, BillHistory
from customer.forms import \
    CreateCustomerForm, \
    CreateInvoiceForm, \
    CreatePackageForm, \
    CreateUnionForm, \
    CreateWordForm, \
    CreateBillForm, \
    BillCheckingFrom


def home_page(request):
    c = None
    if request.method == 'POST':
        form = BillCheckingFrom(request.POST)
        if form.is_valid():
            phone_num_customer_id = form.cleaned_data['phone_num_customer_id']
            if len(phone_num_customer_id[1:11]) == 10:
                try:
                    c = get_object_or_404(Customer, phone_number=int(phone_num_customer_id))
                except:
                    messages.warning(request, "Your Phone number or bill ID is not correct")

            elif len(phone_num_customer_id) == 6:
                try:
                    c = get_object_or_404(Customer, customer_id=phone_num_customer_id)
                except:
                    messages.warning(request, "Your Phone number or bill ID is not correct")

            else:
                messages.warning(request, "Your Phone number or bill ID is not correct")

    else:
        form = BillCheckingFrom()

    return render(request, 'landing-page/main.html', {'form': form, 'c': c})


@login_required()
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers-template/customer_list.html', {'customers': customers})


@login_required(redirect_field_name='/')
def customer_details(request, slug):
    customer = get_object_or_404(Customer, slug=slug)
    # b = Bill.objects.get(customer=customer)
    b = get_object_or_404(Bill, customer=customer)
    last_activate = BillHistory.objects.filter(bill=b).order_by('-created_at')[:1]
    last_activate_date = sum([x.total_days for x in last_activate])
    last_activate_month = round(sum([x.total_days for x in last_activate]) / customer.package_name.month_cycle, 2)
    next_bill_end_date = b.billing_start_date + timedelta(
        days=customer.package_name.month_cycle + customer.package_name.month_cycle)
    current_bill_end_date = b.billing_start_date + timedelta(
        days=customer.package_name.month_cycle)
    customer_invoice = Invoice.objects.filter(bill=b).order_by('-custom_bill_date')
    total_cycle = round(b.total_day / b.customer.package_name.month_cycle, 1)
    context = {'customer': customer,
               'customer_invoice': customer_invoice,
               'next_bill_end_date': next_bill_end_date,
               'current_bill_end_date': current_bill_end_date,
               'total_cycle': total_cycle,
               'last_activate_date': last_activate_date,
               'last_activate_month': last_activate_month,
               }
    return render(request, 'customers-template/customer_details.html', context)


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
    from django.utils import timezone
    customer = Customer.objects.get(customer_id=customer_id)
    bill = Bill.objects.get(customer=customer.id)
    form = CreateInvoiceForm()
    r = HttpResponseRedirect(reverse('customer:customer_details', args=(customer.slug,)))

    if request.method == 'POST':
        form = CreateInvoiceForm(request.POST, request.FILES)
        custom_bill_date = request.POST.get('custom_bill_date')

        custom_date_convert = datetime.strptime(custom_bill_date, "%Y-%m-%d").date()
        same_date_find = [x.custom_bill_date for x in bill.invoice_set.all() if x.custom_bill_date == custom_date_convert]
        if not same_date_find and int(form['invoice_amount'].value()) >= 50:
            if (form['invoice_type'].value() == '3' and
                custom_date_convert > datetime.today().date()) or \
                    (form['invoice_type'].value() in ['0', '2'] and
                     bill.due_bill < 0 and
                     custom_date_convert <= datetime.today().date()) or \
                    form['invoice_type'].value() == '1':
                if form.is_valid():
                    data = form.save(commit=False)
                    data.bill = bill
                    data.invoice_creator = request.user
                    data.custom_bill_date = custom_date_convert
                    data.save()
                    messages.success(request, f"Success, You created invoice for {data} TK. for {custom_date_convert}")
                else:
                    messages.warning(request, f"Data not valid Invoice didn't create {custom_date_convert}")
            else:
                messages.warning(request, f"Invoice not created, please check again! Future Date/No Due")

        else:
            messages.warning(request, f"Invoice not created,  Same date found or minimum amount less than 50 TK")
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


@login_required()
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


@login_required()
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
