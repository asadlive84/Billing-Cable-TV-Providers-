# Generated by Django 2.2.6 on 2019-10-08 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0017_auto_20191009_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='KY6CP5', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
