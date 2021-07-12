from django.contrib import admin
from .models import Product
from .models import QuillPost
# Register your models here.


class QuillPostAdmin(admin.ModelAdmin):
    pass


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')


admin.site.register(Product, ProductAdmin)