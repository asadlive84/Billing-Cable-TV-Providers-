# Generated by Django 2.2.6 on 2019-10-05 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0032_auto_20191006_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='29GK22', max_length=100, verbose_name='Customer ID'),
        ),
    ]
