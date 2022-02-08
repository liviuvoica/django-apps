from django.contrib import admin
from blog_api.models import Category
from blog_api.models import Subcategory
from blog_api.models import Article
from blog_api.models import Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_blog_category_title',
        'get_blog_category_short_description',
        'get_blog_category_is_active',
        'get_owner',
        'created_at',
        'updated_at'
    )
    
    def get_blog_category_title(self, obj):
        return str(obj.blog_category_title).upper()
    get_blog_category_title.short_description = "Category title"
    
    def get_blog_category_short_description(self, obj):
        return str(obj.blog_category_short_description)
    get_blog_category_short_description.short_description = "Short description"
    
    def get_blog_category_is_active(self, obj):
        return str(obj.blog_category_is_active)
    get_blog_category_is_active.short_description = "Is active ?"
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

class SubcategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'blog_category_id',
        'blog_subcategory_title',
        'blog_subcategory_short_description',
        'blog_subcategory_description',
        'blog_subcategory_is_active',
        'blog_subcategory_path',
        'get_owner',
        'created_at',
        'updated_at'
    )
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'blog_subcategory_id',
        'blog_article_author',
        'blog_article_time',
        'blog_article_title',
        'blog_article_short_description',
        'blog_article_content',
        'blog_article_path',
        'blog_article_is_active',
        'blog_article_rating_system',
        'blog_article_likes',
        'blog_article_dislikes',
        'get_owner',
        'created_at',
        'updated_at'
    )

    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'blog_article_id',
        'full_name',
        'email',
        'comment',
        'comment_is_public',
        'privacy_policy',
        'get_owner',
        'created_at',
        'updated_at'
    )

    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)