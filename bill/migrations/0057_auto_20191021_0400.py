# Generated by Django 2.2.6 on 2019-10-20 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0056_auto_20191021_0300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='5353WK', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
