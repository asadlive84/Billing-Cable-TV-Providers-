# Generated by Django 2.2.6 on 2019-10-05 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_auto_20191006_0202'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='slug',
        ),
    ]