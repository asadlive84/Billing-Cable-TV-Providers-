# Generated by Django 2.2.6 on 2019-10-24 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0069_auto_20191025_0200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='4AA245', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='bill',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bill.Bill'),
        ),
    ]