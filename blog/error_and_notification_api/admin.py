from django.contrib import admin
from error_and_notification_api.models import ErrorAndNotification

# Register your models here.

class ErrorAndNotificationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_notify_code',
        'get_notify_short_description',
        'get_notify_reference',
        'created_at',
        'updated_at'
    )

    def get_notify_code(self, obj):
        return str(obj.notify_code)
    get_notify_code.short_description = "Code"

    def get_notify_short_description(self, obj):
        return str(obj.notify_short_description)
    get_notify_short_description.short_description = "Short description"

    def get_notify_reference(self, obj):
        return str(obj.notify_reference)
    get_notify_reference.short_description = "Documentation reference"

admin.site.register(ErrorAndNotification, ErrorAndNotificationAdmin)