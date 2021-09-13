from django.contrib import admin
from .models import Product
from django.utils.html import format_html
from django.contrib.humanize.templatetags.humanize import intcomma
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_format', 'styled_stock')

    def price_format(self, obj):
        price = intcomma(obj.price)
        return f'{price} $'


    def styled_stock(self, obj):
        if obj.stock >= 1000:
            return format_html(f'<span style="color:blue">{obj.stock}</P>')
        elif obj.stock <= 30:
            return format_html(f'<span style="color:red">{obj.stock}</P>')

        else:
            return obj.stock

    price_format.short_description = 'PRICE'

    styled_stock.short_description = 'STOCK'


admin.site.register(Product, ProductAdmin)