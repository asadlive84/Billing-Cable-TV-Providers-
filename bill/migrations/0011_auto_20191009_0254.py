# Generated by Django 2.2.6 on 2019-10-08 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0010_auto_20191009_0253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='2KCL3C', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
