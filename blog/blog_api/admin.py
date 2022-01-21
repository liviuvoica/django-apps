from django.contrib import admin
from blog_api.models import Category
from blog_api.models import Post
from blog_api.models import Comment

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_owner', 'created')
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'get_owner', 'created')
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'get_body', 'get_owner', 'created')
    
    def get_body(self, obj):
        return obj.body[:100] + "..."
    get_body.short_description = "body"
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)