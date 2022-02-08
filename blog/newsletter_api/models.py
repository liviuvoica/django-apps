from datetime import datetime
from django.db import models

# Create your models here.

# Newsletter model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class Newsletter(models.Model):
    full_name = models.CharField(max_length=100, blank=False, default='')
    email = models.CharField(max_length=100, blank=False, default='')
    privacy_policy = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey('auth.User', related_name='subscribers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Newsletter subscribers'
    
    def __str__(self):
        return self.full_name