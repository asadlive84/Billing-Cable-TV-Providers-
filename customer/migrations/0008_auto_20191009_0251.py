# Generated by Django 2.2.6 on 2019-10-08 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20191009_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='6A6A70', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
