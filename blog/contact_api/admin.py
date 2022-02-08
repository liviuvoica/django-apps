from django.contrib import admin
from contact_api.models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'full_name',
        'email',
        'message',
        'privacy_policy',
        'get_owner',
        'created_at',
        'updated_at'
    )

    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

admin.site.register(Contact, ContactAdmin)