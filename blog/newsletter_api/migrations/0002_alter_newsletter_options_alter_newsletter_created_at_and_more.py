# Generated by Django 4.0.1 on 2022-02-08 13:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsletter',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Newsletter subscribers'},
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 17, 57, 962788)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 17, 57, 962788)),
        ),
    ]
