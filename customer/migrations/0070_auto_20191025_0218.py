# Generated by Django 2.2.6 on 2019-10-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0069_auto_20191025_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='028445', max_length=6, unique=True, verbose_name='Customer ID'),
        ),
    ]