from django.db import models

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey('customer.Customer', on_delete=models.CASCADE, verbose_name='customer')
    product = models.ForeignKey('product.Product', on_delete=models.CASCADE, verbose_name='Order_Prod_NAME')
    quantity = models.IntegerField(verbose_name='QUANTITY')
    status = models.CharField(
        choices=(
            ('STANDBY', 'STANDBY'),
            ('PROCESSING', 'PROCESSING'),
            ('PAID', 'PAID'),
            ('REFUNDED', 'REFUNDED'),
        ),
        default='STANDBY', max_length=32, verbose_name='STATUS')
    memo = models.TextField(null=True, blank=True, verbose_name='MEMO')
    registered_date = models.DateTimeField(auto_now_add=True, verbose_name='REGISTERED_DATE')

    def __str__(self):
        return str(self.customer) + ' ' + str(self.product)

    class Meta:
        db_table = 'NewProject_order'
        verbose_name = 'Order'
        verbose_name_plural = 'Order'
