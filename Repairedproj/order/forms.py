import requests
from django import forms
from .models import Order
from customer.models import Customer
from product.models import Product

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
        customer = self.request.sesion.get('user')

        if quantity and product and customer:
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                customer=Customer.objects.get(email=customer)
            )
            order.save()
        else:
            self.add_error('quantity', 'No Data')
            self.add_error('product', 'No Data')
