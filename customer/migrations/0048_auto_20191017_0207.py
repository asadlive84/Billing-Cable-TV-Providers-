# Generated by Django 2.2.6 on 2019-10-16 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0047_auto_20191011_0417'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='91602D', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]