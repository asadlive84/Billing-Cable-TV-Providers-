# Generated by Django 2.2.6 on 2019-10-10 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0041_auto_20191011_0337'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='last_user_has_bill',
            field=models.FloatField(blank=0, default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='PAYYYA', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
