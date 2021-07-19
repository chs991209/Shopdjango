from django.shortcuts import render
from .forms import RegisterForm
from django.views.generic.edit import FormView
# Create your views here.


class OrderCreate(FormView):
    form_class = RegisterForm
    success_url = '/product/'

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })
        return kw