# Generated by Django 4.0.1 on 2022-02-08 10:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_api', '0005_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['created_at'], 'verbose_name_plural': 'Main Categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='posts',
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 12, 0, 51, 833713)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 12, 0, 51, 833713)),
        ),
        migrations.CreateModel(
            name='Subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True, default='', max_length=100)),
                ('body', models.TextField(blank=True, default='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subcategories', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.AddField(
            model_name='category',
            name='blog_subcategories',
            field=models.ManyToManyField(related_name='categories', to='blog_api.Subcategory'),
        ),
    ]