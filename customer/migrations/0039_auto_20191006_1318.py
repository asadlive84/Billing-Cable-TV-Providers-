# Generated by Django 2.2.6 on 2019-10-06 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0038_auto_20191006_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='SM32RP', max_length=100, verbose_name='Customer ID'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_status',
            field=models.CharField(choices=[('0', 'Inactive'), ('1', 'Active')], default='1', max_length=2, verbose_name='Customer Status'),
        ),
    ]
