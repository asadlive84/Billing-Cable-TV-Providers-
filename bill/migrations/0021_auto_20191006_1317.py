# Generated by Django 2.2.6 on 2019-10-06 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0020_auto_20191006_1313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='5KLC65', max_length=6, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='D4F2LL32', max_length=8, verbose_name='Invoice ID'),
        ),
    ]