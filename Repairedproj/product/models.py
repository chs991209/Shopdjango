from django.db import models

# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=256, verbose_name='Prod_NAME')
    price = models.IntegerField(verbose_name='Prod_PRICE')
    description = models.TextField(verbose_name='Prod_DESCRIPTION')
    stock = models.IntegerField(verbose_name='Prod_STOCK')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='ProdREGISTERED_DATE')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'NewProject_product'
        verbose_name = 'PRODUCT'
        verbose_name_plural = 'PRODUCT'

