# Generated by Django 2.2.6 on 2019-10-08 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0012_auto_20191009_0256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='4D5D40', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
