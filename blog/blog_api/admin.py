from django.contrib import admin
from blog_api.models import Category
from blog_api.models import Post
from blog_api.models import Comment

# Register your models here.

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)