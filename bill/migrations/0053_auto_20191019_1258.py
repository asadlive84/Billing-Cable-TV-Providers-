# Generated by Django 2.2.6 on 2019-10-19 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0052_auto_20191019_0508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='WLL4C4', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
