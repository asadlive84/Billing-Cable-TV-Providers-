# Generated by Django 2.2.6 on 2019-10-08 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20191009_0206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='27D444', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
