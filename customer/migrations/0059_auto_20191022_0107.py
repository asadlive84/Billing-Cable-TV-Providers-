# Generated by Django 2.2.6 on 2019-10-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0058_auto_20191022_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='928F88', max_length=6, unique=True, verbose_name='Customer ID'),
        ),
    ]
