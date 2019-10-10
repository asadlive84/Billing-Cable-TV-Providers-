# Generated by Django 2.2.6 on 2019-10-10 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bill', '0031_auto_20191011_0145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='bill_id',
            field=models.CharField(default='C24YA6', max_length=6, unique=True, verbose_name='Bill ID'),
        ),
        migrations.CreateModel(
            name='BillHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_version', models.IntegerField(editable=False)),
                ('text', models.TextField()),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bill.Bill')),
            ],
            options={
                'unique_together': {('date_version', 'bill')},
            },
        ),
    ]
