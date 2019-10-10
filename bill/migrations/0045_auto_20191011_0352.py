# Generated by Django 2.2.6 on 2019-10-10 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0044_auto_20191011_0350'),
    ]

    operations = [
        migrations.AddField(
            model_name='billhistory',
            name='connection_date_end',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='AL2L5A', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]
