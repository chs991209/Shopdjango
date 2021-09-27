from django.db import models


# Create your models here.


class Customer(models.Model):
    email = models.EmailField(verbose_name='email')
    password = models.CharField(
        max_length=128, verbose_name='PASSWORD'
    )
    level = models.CharField(max_length=8, verbose_name='Grade',
                             choices=(
                                 ('admin', 'admin'),
                                 ('user', 'user')
                             ))
    registered_date = models.DateTimeField(auto_now_add=True,
                                           verbose_name='REGISTERED_DATE'
                                           )

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'NewProject_customer'
        verbose_name = 'Users'
        verbose_name_plural = 'Users'
