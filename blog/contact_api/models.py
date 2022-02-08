from datetime import datetime
from django.db import models

# Create your models here.

# Contact model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class Contact(models.Model):
    full_name = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    message = models.CharField(max_length=255, blank=False, default='')
    privacy_policy = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey('auth.User', related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Contact me'
    
    def __str__(self):
        return self.name