# Generated by Django 2.2.6 on 2019-10-22 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0063_auto_20191022_2007'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='customer_status',
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='164084', max_length=6, unique=True, verbose_name='Customer ID'),
        ),
    ]
