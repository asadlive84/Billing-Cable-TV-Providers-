# Generated by Django 2.2.6 on 2019-10-06 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0041_auto_20191006_2247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='52CPK5', max_length=6, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='LLDKPPDP', max_length=8, verbose_name='Invoice ID'),
        ),
    ]
