# Generated by Django 3.2.5 on 2021-08-17 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_alter_customer_email'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customerclass', 'verbose_name_plural': 'customerclass'},
        ),
        migrations.AlterField(
            model_name='customer',
            name='level',
            field=models.CharField(choices=[('admin', 'admin'), ('user', 'user')], max_length=8, verbose_name='Grade'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='registered_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='REGISTERED_DATE'),
        ),
    ]
