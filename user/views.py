from datetime import timedelta

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import permission_required
from django.db.models import Sum
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

from bill.models import Invoice, Bill
from user.models import CustomUser
from user.forms import CustomUserCreationForm, PermissionRuleForm
import re
from django.contrib import messages


def sign_up_form(request):
    if not request.user.is_authenticated:
        regex_pattern = '(^[01]{1,2})([3456789]{1})(\d{2})(\d{6})$'
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST, request.FILES)
            get_phone_number = form['phone_number'].value()
            raw_password = form['password1']

            phone_regex = int(re.match(regex_pattern, get_phone_number)[0])
            if raw_password != phone_regex:
                if form.is_valid():
                    data = form.save(commit=False)
                    raw_password = form.cleaned_data.get('password1')
                    data.phone_number = phone_regex
                    data.is_staff = False
                    data.save()

                    # permission set up
                    content_type = ContentType.objects.get_for_model(CustomUser)
                    content_type_id = ContentType.objects.get_for_id(data.id)
                    permission = Permission.objects.create(
                        codename='can_view_self_profile',
                        name='Can view self profile only',
                        content_type=content_type,
                        content_type_id=content_type_id,
                    )
                    data.user_permissions.set([permission])

                    user = authenticate(phone_number=data.phone_number, password=raw_password)
                    login(request, user)

                    messages.success(request, "User has been successfully created!!")

                    return HttpResponseRedirect(reverse('user_details', args=[user.pk]))

                else:
                    messages.warning(request, "User not created!!")
            else:
                messages.warning(request, f"Phone number and password can't be same")

        else:
            form = CustomUserCreationForm()

        return render(request, 'signup.html', {'form': form, })

    else:
        return redirect('customer:home')


@permission_required('customuser.view_customuser')
def user_list(request):
    users = CustomUser.objects.all()
    return render(request, 'customers-template/user_list.html', {'users': users})


def user_details(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)
    customer_invoice = Invoice.objects.filter(invoice_creator=user)
    if request.method == "POST":
        from_date = request.POST.get('id_custom_bill_date1')
        to_date = request.POST.get('id_custom_bill_date2', timezone.now().date())
        customer_invoice = Invoice.objects.filter(invoice_creator=user,
                                                  custom_bill_date__gte=from_date,
                                                  custom_bill_date__lte=to_date,
                                                  )

        total_taka = customer_invoice.aggregate(invoice_amount=Sum('invoice_amount'))
        context = {
            'user': user,
            'customer_invoice': customer_invoice,
            'to_date': to_date,
            'from_date': from_date,
            'total_taka': total_taka,
        }
        return render(request, 'customers-template/user_details.html', context)

    return render(request, 'customers-template/user_details.html', {'user': user, 'customer_invoice': customer_invoice})


def permission_setup(request, pk):
    user = get_object_or_404(CustomUser, pk=pk)

    customer_invoice = Invoice.objects.filter(invoice_creator=user)

    if request.method == "POST":
        form = PermissionRuleForm(request.POST or None, instance=user)

        if form.is_valid():
            form.save()
            messages.success(request, f"Permission changed!")
    else:
        form = PermissionRuleForm(instance=user)
    return render(request, 'customers-template/permission_setup.html',
                  {'user': user, 'form': form})
