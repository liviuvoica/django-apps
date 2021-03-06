# Generated by Django 4.0.1 on 2022-02-08 10:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0007_alter_subcategory_options_remove_subcategory_body_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='owner',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Subcategories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 12, 26, 4, 5508)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 12, 26, 4, 5508)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 12, 26, 4, 6509)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 12, 26, 4, 6509)),
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
