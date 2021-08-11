from django import forms
from .models import Product
from django.contrib.auth.hashers import make_password, check_password


class RegisterForm(forms.Form):
    name = forms.CharField(
        error_messages={
            'required': 'Enter Product Name'
        },
        label='Product Name'
    )
    price = forms.IntegerField(
        error_messages={
            'required': 'Enter Product'
        }, label='Product Price'
    )
    description = forms.CharField(
        error_messages={
            'required': 'Enter Product Description'
        }, label='Product Description'
    )
    stock = forms.IntegerField(
        error_messages={
                             'required': 'Enter Product Stock'
        }, label='Stock'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        if not(name and price and description and stock):
            self.add_error('name', 'No Value')
            self.add_error('price', 'No Value')
