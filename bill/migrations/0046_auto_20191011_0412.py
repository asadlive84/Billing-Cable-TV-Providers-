# Generated by Django 2.2.6 on 2019-10-10 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0045_auto_20191011_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='6K6WC6', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
