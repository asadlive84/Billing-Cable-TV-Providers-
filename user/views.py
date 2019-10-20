from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from user.models import CustomUser
from user.forms import CustomUserCreationForm
import re
from django.contrib import messages


def sign_up_form(request):
    if not request.user.is_authenticated:
        regex_pattern = '(^[01]{1,2})([3456789]{1})(\d{2})(\d{6})$'
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST, request.FILES)
            get_phone_number = form['phone_number'].value()
            raw_password = form['password1']

            try:
                phone_regex = int(re.match(regex_pattern, get_phone_number)[0])
                if raw_password != phone_regex:
                    if form.is_valid():
                        data = form.save(commit=False)
                        raw_password = form.cleaned_data.get('password1')
                        data.phone_number = phone_regex
                        data.is_staff = False
                        data.save()

                        user = authenticate(phone_number=data.phone_number, password=raw_password)
                        login(request, user)
                        return redirect('customer:home')

                        messages.success(request, "User has been successfully created!!")

                    else:
                        messages.warning(request, "User not created!!")
                else:
                    messages.warning(request, f"Phone number and password can't be same")
            except Exception as e:
                messages.warning(request, f"Phone number Format isn't correct!")
        else:
            form = CustomUserCreationForm()

        return render(request, 'signup.html', {'form': form, })

    else:
        return redirect('customer:home')
