# Generated by Django 2.2.6 on 2019-10-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0026_auto_20191009_2108'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='invoice_bill_collector',
            field=models.FloatField(blank=0, default=0, null=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='WK6LKA', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
