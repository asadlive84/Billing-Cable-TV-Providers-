from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django import forms
from user.models import CustomUser
import re
from django.contrib.auth.models import Permission


class UserLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.IntegerField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Mobile number Ex 017....'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
        }))


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.IntegerField(required=True, help_text="Type you phone number BD format 01712123456")
    full_name = forms.CharField(max_length=100, help_text="Type your Full Name")

    class Meta:
        model = CustomUser
        fields = ('full_name', 'phone_number', 'username')

    # def clean_phone_number(self):
    #     pattern = '(^[01]{1,2})([13456789]{1})(\d{2})(\d{6})$'
    #
    #     phone_number = self.cleaned_data["phone_number"]
    #     phone_regex_num = int(re.match(pattern, phone_number)[0])
    #     try:
    #         CustomUser.objects.get(phone_number=phone_regex_num)
    #     except CustomUser.DoesNotExist:
    #         return phone_number
    #     raise forms.ValidationError(_("A user with that phone number already exists."))


class PermissionRuleForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('is_staff', 'is_active', 'user_type',)

    def __init__(self, *args, **kwargs):
        super(PermissionRuleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
