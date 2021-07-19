from django import forms
from .models import Order


class RegisterForm(forms.Form):

    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request

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
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
