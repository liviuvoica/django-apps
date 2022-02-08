# Generated by Django 4.0.1 on 2022-02-08 12:53

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0012_alter_article_created_at_alter_article_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 983309)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 983309)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 981309)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 981309)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 984307)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 984307)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 982308)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 53, 1, 982308)),
        ),
    ]