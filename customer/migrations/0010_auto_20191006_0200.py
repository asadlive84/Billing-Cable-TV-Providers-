# Generated by Django 2.2.6 on 2019-10-05 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0009_auto_20191006_0150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Customer ID'),
        ),
    ]
