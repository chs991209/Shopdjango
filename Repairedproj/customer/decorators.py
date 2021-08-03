from django.shortcuts import redirect
from .models import Customer


def login_required(function):
    def wrap(request, *args, **kwargs):
        customer = request.session.get('customer')
        if customer is None or not customer:
            return redirect('/login')
        return function(request, *args, **kwargs)

    return wrap


def admin_required(function):
    def wrap(request, *args, **kwargs):
        customer = request.session.get('customer')
        if customer is None or not customer:
            return redirect('/login')

        customer = Customer.objects.get(email=customer)
        if customer.level !='admin':
            return redirect('/')

        return function(request, *args, **kwargs)

    return wrap



