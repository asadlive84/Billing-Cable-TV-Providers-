# Generated by Django 2.2.6 on 2019-10-22 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0066_auto_20191023_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='8FA949', max_length=6, unique=True, verbose_name='Customer ID'),
        ),
    ]
