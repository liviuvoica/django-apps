from datetime import datetime
from django.db import models

# Create your models here.

# Error and Notification model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class ErrorAndNotification(models.Model):
    notify_code = models.CharField(max_length=100, blank=False, default='')
    notify_short_description = models.CharField(max_length=255, blank=False, default='')
    notify_reference = models.CharField(max_length=255, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='error_and_notifications', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Error and Notifications Messages'
    
    def __str__(self):
        return self.name