# Generated by Django 2.2.6 on 2019-10-10 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0035_auto_20191011_0243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='67A479', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
