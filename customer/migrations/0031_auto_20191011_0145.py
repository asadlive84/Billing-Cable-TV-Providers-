# Generated by Django 2.2.6 on 2019-10-10 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0030_auto_20191011_0114'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='5F4164', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]