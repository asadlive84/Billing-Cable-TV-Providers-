# Generated by Django 2.2.6 on 2019-10-08 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0006_auto_20191009_0239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='74175D', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]