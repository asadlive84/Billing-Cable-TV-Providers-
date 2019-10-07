# Generated by Django 2.2.6 on 2019-10-06 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0026_auto_20191006_1339'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bill',
            name='total_due_bill',
        ),
        migrations.AddField(
            model_name='bill',
            name='due_bill',
            field=models.FloatField(default=0, verbose_name='Due Bill'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='6A5C65', max_length=6, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='due_bill_status',
            field=models.BooleanField(default=True, verbose_name='Due Status'),
        ),
        migrations.AlterField(
            model_name='bill',
            name='total_bill',
            field=models.FloatField(default=0, verbose_name='Total Bill'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='K4334LP4', max_length=8, verbose_name='Invoice ID'),
        ),
    ]