from datetime import datetime
from django.db import models

# Create your models here.

# Blog categories model will have a many to one relationship
# with the User model via 'owner' foreign key and a many to many relationship with
# the Post model via 'post' foreign key
# related_name refers to a custom access name for the current model
class Category(models.Model):
    blog_category_title = models.CharField(max_length=100, blank=False, default='')
    blog_category_short_description = models.CharField(max_length=255, blank=False, default='')
    blog_category_description = models.TextField(blank=False, default='')
    blog_category_is_active = models.BooleanField(blank=False, default=False)
    blog_image_card_url = models.CharField(max_length=255, blank=False, default='')
    blog_category_path = models.CharField(max_length=255, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='categories', on_delete=models.CASCADE)
    blog_subcategories = models.ManyToManyField('Subcategory', related_name='subcategories', blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.blog_category_title

# Blog subcategories model will have a many to one relationship
# with the User model via 'owner' foreign key and a many to many relationship with
# the Subcategory model via 'blog_subcategory' foreign key
# related_name refers to a custom access name for the current model
class Subcategory(models.Model):
    blog_category_id = models.ForeignKey('blog_api.Category', related_name='subcategories', on_delete=models.CASCADE, default=1)
    blog_subcategory_title = models.CharField(max_length=100, blank=False, default='')
    blog_subcategory_short_description = models.CharField(max_length=255, blank=False, default='')
    blog_subcategory_description = models.TextField(blank=False, default='')
    blog_subcategory_is_active = models.BooleanField(blank=False, default=False)
    blog_subcategory_path = models.CharField(max_length=255, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='subcategories', on_delete=models.CASCADE)
    blog_articles = models.ManyToManyField('Article', related_name='articles', blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Subcategories'
    
    def __str__(self):
        return self.blog_subcategory_title

# Blog articles model will have a many to one relationship
# with the User model via 'owner' foreign key and a many to many relationship with
# the Subcategory model via 'blog_subcategory' foreign key
# related_name refers to a custom access name for the current model
class Article(models.Model):
    blog_subcategory_id = models.ForeignKey('blog_api.Subcategory', related_name='articles', on_delete=models.CASCADE, default=1)
    blog_article_author = models.CharField(max_length=100, blank=False, default='')
    blog_article_time = models.IntegerField(blank=False, default='')
    blog_article_title = models.CharField(max_length=100, blank=False, default='')
    blog_article_short_description = models.CharField(max_length=255, blank=False, default='')
    blog_article_content = models.TextField(blank=False, default='')
    blog_article_path = models.CharField(max_length=255, blank=False, default='')
    blog_article_is_active = models.BooleanField(blank=False, default=False)
    blog_article_rating_system = models.IntegerField(blank=False, default='')
    blog_article_likes = models.IntegerField(blank=False, default='')
    blog_article_dislikes = models.IntegerField(blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='articles', on_delete=models.CASCADE)
    blog_article_comments = models.ManyToManyField('Comment', related_name='comments', blank=True)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Articles'
    
    def __str__(self):
        return self.blog_article_title

# Blog article comments model will have a many to one relationship
# with the User model via 'owner' foreign key and a many to many relationship with
# the Subcategory model via 'blog_subcategory' foreign key
# related_name refers to a custom access name for the current model
class Comment(models.Model):
    blog_article_id = models.ForeignKey('blog_api.Article', related_name='comments', on_delete=models.CASCADE, default=1)
    full_name = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    comment = models.CharField(max_length=255, blank=False, default='')
    comment_is_public = models.BooleanField(blank=False, default=False)
    privacy_policy = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())
    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Article comments'
    
    def __str__(self):
        return self.full_name