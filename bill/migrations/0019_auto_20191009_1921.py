# Generated by Django 2.2.6 on 2019-10-09 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0018_auto_20191009_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='YW3YCP', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_type',
            field=models.CharField(choices=[('0', 'Due Bill'), ('1', 'New Connection'), ('2', 'Current Bill'), ('3', 'Advance Bill')], default='2', max_length=1),
        ),
    ]
