# Generated by Django 2.2.6 on 2019-10-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0018_auto_20191009_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='988581', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
