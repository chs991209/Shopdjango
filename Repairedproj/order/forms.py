from django import forms
from .models import Order


class RegisterForm(forms.Form):
    quantity = forms.IntegerField(
        error_messages={
            'required': 'Enter the quantity'
        }, label='Quantity'
    )
    product = forms.IntegerField(
        error_messages={
            'required': 'Enter Product Name'
        }, label='Product Description', widget=forms.HiddenInput
    )

    def clean(self):
        cleaned_data = super().clean()
