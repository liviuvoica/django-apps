from django.contrib import admin
from newsletter_api.models import Newsletter

# Register your models here.

class NewsletterAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'privacy_policy',
        'get_owner',
        'created_at',
        'updated_at'
    )

    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

admin.site.register(Newsletter, NewsletterAdmin)