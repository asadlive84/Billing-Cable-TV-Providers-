# Generated by Django 2.2.6 on 2019-10-06 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0051_auto_20191006_1406'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='PE61KP', max_length=100, verbose_name='Customer ID'),
        ),
        migrations.AlterField(
            model_name='package',
            name='package_bill',
            field=models.FloatField(default=0, verbose_name='Per Month Amount'),
        ),
    ]