# Generated by Django 2.2.6 on 2019-10-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_auto_20191009_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='229355', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
