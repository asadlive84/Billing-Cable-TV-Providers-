# Generated by Django 2.2.6 on 2019-10-10 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0034_auto_20191011_0240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billhistory',
            old_name='text_date',
            new_name='connection_date_new',
        ),
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='2K3KLW', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
    ]