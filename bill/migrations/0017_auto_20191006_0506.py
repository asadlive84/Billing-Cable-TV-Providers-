# Generated by Django 2.2.6 on 2019-10-05 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0016_auto_20191006_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='CLP4#P', max_length=6, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='56F322DD', max_length=8, verbose_name='Invoice ID'),
        ),
    ]