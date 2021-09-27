from django.contrib import admin
from .models import Customer

# Register your models here.


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('email',)

    def changelist_view(self, request, extra_context=None):
        extra_context = {'title': 'UserList' }
        return super().changelist_view(request, extra_context)
    
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        customer = Customer.objects.get(pk=object_id)
        extra_context = {'title': f'{customer.email}수정하기'}
        return super().changeform_view(request, object_id, form_url, extra_context)


        


admin.site.register(Customer, CustomerAdmin)