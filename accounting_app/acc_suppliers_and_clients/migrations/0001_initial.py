# Generated by Django 4.0.1 on 2022-02-28 15:28

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('trade_register_registration_number', models.CharField(default='', max_length=15)),
                ('fiscal_code', models.CharField(default='', max_length=9)),
                ('analytical_account', models.CharField(default='', max_length=13)),
                ('county', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('bank_account', models.CharField(default='', max_length=24)),
                ('bank_name', models.CharField(default='', max_length=255)),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('email_address', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 17, 28, 5, 983398))),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 17, 28, 5, 983398))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suppliers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Suppliers',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('trade_register_registration_number', models.CharField(default='', max_length=15)),
                ('fiscal_code', models.CharField(default='', max_length=9)),
                ('pin', models.CharField(default='', max_length=13)),
                ('analytical_account', models.CharField(default='', max_length=13)),
                ('county', models.CharField(default='', max_length=255)),
                ('city', models.CharField(default='', max_length=255)),
                ('address', models.CharField(default='', max_length=255)),
                ('bank_account', models.CharField(default='', max_length=24)),
                ('bank_name', models.CharField(default='', max_length=255)),
                ('phone_number', models.CharField(default='', max_length=10)),
                ('email_address', models.CharField(default='', max_length=100)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 17, 28, 5, 986584))),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 28, 17, 28, 5, 986584))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='clients', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Clients',
                'ordering': ['created_at'],
            },
        ),
    ]
