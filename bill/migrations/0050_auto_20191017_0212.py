# Generated by Django 2.2.6 on 2019-10-16 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0049_auto_20191017_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='34WC55', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]