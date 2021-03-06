# Generated by Django 2.2.6 on 2019-10-08 20:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.CharField(default='8D7505', max_length=100, unique=True, verbose_name='Customer ID')),
                ('name', models.CharField(max_length=200, verbose_name='Customer Name')),
                ('customer_status', models.CharField(choices=[('0', 'Inactive'), ('1', 'Active')], default='1', max_length=2, verbose_name='Customer Status')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1, verbose_name='Gender')),
                ('phone_number', models.IntegerField(db_index=True, unique=True)),
                ('email_field', models.EmailField(blank=True, max_length=254, null=True)),
                ('alter_phone_number', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('total_due', models.FloatField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('package_name', models.CharField(default='', max_length=100, verbose_name='Package')),
                ('package_bill', models.FloatField(default=0, verbose_name='Per Month Amount')),
                ('month_cycle', models.IntegerField(default=30, verbose_name='Month Cycle')),
                ('per_day_amount', models.FloatField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Union',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('union_name', models.CharField(max_length=100)),
                ('union_number', models.IntegerField()),
                ('help_info', models.CharField(blank=True, max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_name', models.CharField(max_length=100)),
                ('word_number', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('union', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Union')),
            ],
        ),
    ]
