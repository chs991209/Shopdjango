# Generated by Django 3.2.4 on 2021-06-17 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256, verbose_name='Prod_NAME')),
                ('price', models.IntegerField(verbose_name='Prod_PRICE')),
                ('description', models.TextField(verbose_name='Prod_DESCRIPTION')),
                ('stock', models.IntegerField(verbose_name='Prod_STOCK')),
                ('registered_date', models.DateTimeField(auto_now_add=True, verbose_name='ProdREGISTERED_DATE')),
            ],
            options={
                'verbose_name': 'PRODUCT',
                'verbose_name_plural': 'PRODUCT',
                'db_table': 'NewProject_product',
            },
        ),
    ]
