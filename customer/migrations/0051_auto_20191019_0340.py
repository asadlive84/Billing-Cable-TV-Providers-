# Generated by Django 2.2.6 on 2019-10-18 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0050_auto_20191017_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='806D30', max_length=6, unique=True, verbose_name='Customer ID'),
        ),
    ]
