# Generated by Django 2.2.6 on 2019-10-25 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0077_auto_20191025_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='47F2DF', max_length=6, unique=True, verbose_name='Customer ID'),
        ),
    ]