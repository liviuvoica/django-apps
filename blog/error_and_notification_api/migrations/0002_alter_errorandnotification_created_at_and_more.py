# Generated by Django 4.0.1 on 2022-02-08 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('error_and_notification_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='errorandnotification',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 27, 37, 482116)),
        ),
        migrations.AlterField(
            model_name='errorandnotification',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 27, 37, 482116)),
        ),
    ]
