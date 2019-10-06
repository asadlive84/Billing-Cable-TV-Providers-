# Generated by Django 2.2.6 on 2019-10-06 22:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0070_auto_20191007_0433'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='created_user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.CharField(default='61A787', max_length=100, unique=True, verbose_name='Customer ID'),
        ),
    ]
