# Generated by Django 2.2.6 on 2019-10-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0042_auto_20191006_1339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='CQP1KG', max_length=100, verbose_name='Customer ID'),
        ),
    ]
