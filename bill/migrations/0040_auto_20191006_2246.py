# Generated by Django 2.2.6 on 2019-10-06 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0039_auto_20191006_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='4YAA#6', max_length=6, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='DP526K35', max_length=8, verbose_name='Invoice ID'),
        ),
    ]