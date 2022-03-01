# Generated by Django 4.0.1 on 2022-03-01 08:03

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('acc_operations', '0002_alter_purchaseinvoice_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 10, 3, 35, 477333)),
        ),
        migrations.AlterField(
            model_name='purchaseinvoice',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 10, 3, 35, 477333)),
        ),
        migrations.CreateModel(
            name='SalesInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='', max_length=100)),
                ('invoice_number', models.CharField(default='', max_length=15)),
                ('invoice_series', models.CharField(default='', max_length=15)),
                ('client_code', models.CharField(default='', max_length=5)),
                ('client_name', models.CharField(default='', max_length=255)),
                ('client_vat', models.BooleanField(default=False)),
                ('invoice_date', models.DateField(default='')),
                ('invoice_due_date', models.DateField(default='')),
                ('invoice_gross_value', models.IntegerField(default=0)),
                ('invoice_vat_value', models.IntegerField(default=0)),
                ('invoice_net_value', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 10, 3, 35, 478341))),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 10, 3, 35, 478341))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_invoices', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Facturi de Vanzare',
                'ordering': ['created_at'],
            },
        ),
    ]