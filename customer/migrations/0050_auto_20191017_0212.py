# Generated by Django 2.2.6 on 2019-10-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0049_auto_20191017_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='0F2327', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
