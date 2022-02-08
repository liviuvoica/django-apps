# Generated by Django 4.0.1 on 2022-02-08 09:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0004_alter_category_options_alter_post_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.RenameField(
            model_name='category',
            old_name='name',
            new_name='blog_category_title',
        ),
        migrations.RemoveField(
            model_name='category',
            name='created',
        ),
        migrations.AddField(
            model_name='category',
            name='blog_category_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='category',
            name='blog_category_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='category',
            name='blog_category_path',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='blog_category_short_description',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='blog_image_card_url',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 11, 49, 10, 274375)),
        ),
        migrations.AddField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 11, 49, 10, 274375)),
        ),
    ]
