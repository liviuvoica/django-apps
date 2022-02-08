# Generated by Django 4.0.1 on 2022-02-08 13:17

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
            name='ErrorAndNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('notify_code', models.CharField(default='', max_length=100)),
                ('notify_short_description', models.CharField(default='', max_length=255)),
                ('notify_reference', models.CharField(default='', max_length=255)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 17, 57, 984796))),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 15, 17, 57, 984796))),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='error_and_notifications', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Error and Notifications Messages',
                'ordering': ['created_at'],
            },
        ),
    ]