# Generated by Django 2.2.6 on 2019-10-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0009_auto_20191009_0251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='624L3P', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
