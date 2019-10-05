# Generated by Django 2.2.6 on 2019-10-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0022_auto_20191006_0323'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='email_field',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='4PEP97', max_length=100, verbose_name='Customer ID'),
        ),
    ]
