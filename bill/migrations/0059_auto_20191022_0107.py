# Generated by Django 2.2.6 on 2019-10-21 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0058_auto_20191022_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='C432P4', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
