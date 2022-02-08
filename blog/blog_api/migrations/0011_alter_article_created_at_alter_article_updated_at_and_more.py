# Generated by Django 4.0.1 on 2022-02-08 12:07

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog_api', '0010_alter_article_created_at_alter_article_updated_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 589687)),
        ),
        migrations.AlterField(
            model_name='article',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 589687)),
        ),
        migrations.AlterField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 587689)),
        ),
        migrations.AlterField(
            model_name='category',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 587689)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='created_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 588688)),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 588688)),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='', max_length=100)),
                ('email', models.CharField(default='', max_length=100)),
                ('comment', models.CharField(default='', max_length=255)),
                ('comment_is_public', models.BooleanField(default=False)),
                ('privacy_policy', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 590687))),
                ('updated_at', models.DateTimeField(blank=True, default=datetime.datetime(2022, 2, 8, 14, 7, 47, 590687))),
                ('blog_article_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog_api.article')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Article comments',
                'ordering': ['created_at'],
            },
        ),
        migrations.AddField(
            model_name='article',
            name='blog_article_comments',
            field=models.ManyToManyField(related_name='comments', to='blog_api.Comment'),
        ),
    ]
