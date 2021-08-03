from django.shortcuts import redirect


def login_required(function):
    def wrap(request, *args, **kwargs):
        customer = request.session.get('customer')
        if customer is None or not customer:
            return redirect('/login')
        print('If you want to use this page, you need to login')
        return function(request, *args, **kwargs)

    return wrap