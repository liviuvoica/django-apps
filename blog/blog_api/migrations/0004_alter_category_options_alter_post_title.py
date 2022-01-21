# Generated by Django 4.0.1 on 2022-01-21 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_api', '0003_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created'], 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.TextField(blank=True, default='', max_length=100),
        ),
    ]
