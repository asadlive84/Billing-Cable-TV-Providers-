# Generated by Django 2.2.6 on 2019-10-10 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0029_auto_20191010_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='due_bill',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='56YL4Y', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
