# Generated by Django 2.2.6 on 2019-10-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0053_auto_20191019_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='L6LA4A', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
