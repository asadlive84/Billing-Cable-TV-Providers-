# Generated by Django 2.2.6 on 2019-10-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0022_auto_20191009_2041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='KKL63P', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]