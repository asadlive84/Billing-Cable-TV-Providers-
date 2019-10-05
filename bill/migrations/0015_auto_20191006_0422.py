# Generated by Django 2.2.6 on 2019-10-05 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0014_auto_20191006_0414'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='adjustment',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='invoice_id',
            field=models.CharField(db_index=True, default='D2F553KK', max_length=8, verbose_name='Invoice ID'),
        ),
    ]