# Generated by Django 2.2.6 on 2019-10-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_auto_20191009_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='DF3661', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]