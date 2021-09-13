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
        stock = obj.stock
        if stock >= 1000:
            stock = intcomma(stock)
            return format_html(f'<b><span style="color:blue">{stock} 개</b>')
        elif stock <= 30:
            stock = intcomma(stock)
            return format_html(f'<b><span style="color:red">{stock} 개</b>')

        return format_html (f'<b>{intcomma(stock)} 개</b>')

    price_format.short_description = 'PRICE'

    styled_stock.short_description = 'STOCK'


admin.site.register(Product, ProductAdmin)