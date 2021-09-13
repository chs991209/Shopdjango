from django.contrib import admin
from .models import Order
from django.utils.html import format_html

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_filter = ('status',)
    list_display = ('customer', 'product', 'styled_status')

    def styled_status(self, obj):
        if obj.status == 'REFUNDED':
            return format_html(f'<span style="color:red">{obj.status}</p>')
        if obj.status == 'STANDBY':
            return format_html(f'<span style="color:blue">{obj.status}</p>')
        if obj.status == 'PAID':
            return format_html(f'<span style="color:green">{obj.status}</p>')
        if obj.status == 'PROCESSING':
            return format_html(f'<span style="color:brown">{obj.status}</p>') #f>>바로 입력

        return obj.status

    styled_status.short_description = 'STATUS'


admin.site.register(Order, OrderAdmin)