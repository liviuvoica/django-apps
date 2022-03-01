# Generated by Django 4.0.1 on 2022-03-01 07:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acc_suppliers_and_clients', '0004_alter_article_created_at_alter_article_current_stock_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 806811)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 806811)),
        ),
        migrations.AlterField(
            model_name='chartofaccount',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 806811)),
        ),
        migrations.AlterField(
            model_name='chartofaccount',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 806811)),
        ),
        migrations.AlterField(
            model_name='client',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 805764)),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 805764)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 803764)),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 3, 1, 9, 54, 23, 803764)),
        ),
    ]