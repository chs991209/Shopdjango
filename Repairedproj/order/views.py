from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from customer.decorators import login_required
from .models import Order
from django.db import transaction
from product.models import Product
from customer.models import Customer
from .forms import RegisterForm
# Create your views here.


@method_decorator(login_required, name='dispatch')
class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def form_valid(self, form):
        with transaction.atomic():
            product = Product.objects.get(pk=product)
            order = Order(
                quantity=quantity,
                product=Product.objects.get(pk=product),
                customer=Customer.objects.get(email=customer)
            )
            order.save()
            product.stock -= quantity
            product.save()

            return super().form_valid(form)

    def form_invalid(self, form):
        return redirect('/product/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw


@method_decorator(login_required, name='dispatch')
class OrderList(ListView):
    template_name = 'order.html'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(customer__email=self.request.session.get('user'))
        return queryset
