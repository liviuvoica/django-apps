# Generated by Django 4.0.1 on 2022-02-08 13:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter_api', '0002_alter_newsletter_options_alter_newsletter_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 27, 37, 481116)),
        ),
        migrations.AlterField(
            model_name='newsletter',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 27, 37, 481116)),
        ),
    ]