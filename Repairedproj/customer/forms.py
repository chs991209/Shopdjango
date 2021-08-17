from django import forms
from .models import Customer
from django.contrib.auth.hashers import check_password


class RegisterForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Enter Email'
        },
        max_length=64, label='Email'
    )
    password = forms.CharField(
        error_messages={
            'required': 'Enter Password'
        },
        widget=forms.PasswordInput, label='Password'
    )
    re_password = forms.CharField(
        error_messages={
            'required': 'Enter Password'
        },
        widget=forms.PasswordInput, label='Password Check')

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password and re_password:
            if password != re_password:
                self.add_error('password', 'Password Not Identical')
                self.add_error('re_password', 'Password Not Identical')


class LoginForm(forms.Form):
    email = forms.EmailField(
        error_messages={
            'required': 'Enter Email'
        },
        max_length=64, label='Email'
    )
    password = forms.CharField(
        error_messages={
            'required': 'Enter Password'
        },
        widget=forms.PasswordInput, label='Password'
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if email and password:
            try:
                customer = Customer.objects.get(email=email)
            except Customer.DoesNotExist:
                self.add_error('email', 'Not an Existing ID')
                return

            if not check_password(password, customer.password):
                self.add_error('password', 'Incorrect Password')
