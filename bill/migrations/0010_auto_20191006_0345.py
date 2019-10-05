# Generated by Django 2.2.6 on 2019-10-05 21:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0009_auto_20191006_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invoice',
            name='customer',
        ),
        migrations.AddField(
            model_name='invoice',
            name='bill_customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bill.Bill'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='P3D6P664', max_length=8, verbose_name='Invoice ID'),
        ),
    ]