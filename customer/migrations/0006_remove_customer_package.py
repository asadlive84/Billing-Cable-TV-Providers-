# Generated by Django 2.2.6 on 2019-10-05 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20191006_0148'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='package',
        ),
    ]