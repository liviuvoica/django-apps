from curses import flash
from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

# Supplier model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class Supplier(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    trade_register_registration_number = models.CharField(max_length=15, blank=False, default='')
    fiscal_code = models.CharField(max_length=9, blank=False, default='')
    analytical_account = models.CharField(max_length=13, blank=False, default='')
    county = models.CharField(max_length=255, blank=False, default='')
    city = models.CharField(max_length=255, blank=False, default='')
    address = models.CharField(max_length=255, blank=False, default='')
    bank_account = models.CharField(max_length=24, blank=False, default='')
    bank_name = models.CharField(max_length=255, blank=False, default='')
    phone_number = models.CharField(max_length=10, blank=False, default='')
    email_address = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='suppliers', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Furnizori'
    
    def __str__(self):
        return self.name


# Client model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class Client(models.Model):
    name = models.CharField(max_length=100, blank=False, default='')
    trade_register_registration_number = models.CharField(max_length=15, blank=False, default='')
    fiscal_code = models.CharField(max_length=9, blank=False, default='')
    pin = models.CharField(max_length=13, blank=False, default='')
    analytical_account = models.CharField(max_length=13, blank=False, default='')
    county = models.CharField(max_length=255, blank=False, default='')
    city = models.CharField(max_length=255, blank=False, default='')
    address = models.CharField(max_length=255, blank=False, default='')
    bank_account = models.CharField(max_length=24, blank=False, default='')
    bank_name = models.CharField(max_length=255, blank=False, default='')
    phone_number = models.CharField(max_length=10, blank=False, default='')
    email_address = models.CharField(max_length=100, blank=False, default='')
    owner = models.ForeignKey('auth.User', related_name='clients', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Clienti'
    
    def __str__(self):
        return self.name


# ChartOfAccount model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class ChartOfAccount(models.Model):
    account = models.CharField(max_length=13, blank=False, default='')
    name = models.CharField(max_length=255, blank=False, default='')
    type = models.CharField(max_length=1, blank=False, default='')
    is_active = models.BooleanField(blank=False, default=False)
    owner = models.ForeignKey('auth.User', related_name='chart_of_accounts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Plan de conturi'
    
    def __str__(self):
        return self.name