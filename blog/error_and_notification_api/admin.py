from django.contrib import admin
from error_and_notification_api.models import ErrorAndNotification

# Register your models here.

class ErrorAndNotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'notify_code',
        'notify_short_description',
        'notify_reference',
        'get_owner',
        'created_at',
        'updated_at'
    )

    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

admin.site.register(ErrorAndNotification, ErrorAndNotificationAdmin)