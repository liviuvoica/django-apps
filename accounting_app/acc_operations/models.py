from curses import flash
from datetime import datetime
from email.policy import default
from django.db import models

# Create your models here.

# PurchaseInvoice model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class PurchaseInvoice(models.Model):
    type = models.CharField(max_length=100, blank=False, default='')
    invoice_number = models.CharField(max_length=15, blank=False, default='')
    invoice_series = models.CharField(max_length=15, blank=False, default='')
    supplier_code = models.CharField(max_length=5, blank=False, default='')
    supplier_name = models.CharField(max_length=255, blank=False, default='')
    supplier_vat = models.BooleanField(blank=False, default=False)
    invoice_date = models.DateField(blank=False, default='')
    invoice_due_date = models.DateField(blank=False, default='')
    invoice_gross_value = models.IntegerField(blank=False, default=0)
    invoice_vat_value = models.IntegerField(blank=False, default=0)
    invoice_net_value = models.IntegerField(blank=False, default=0)
    owner = models.ForeignKey('auth.User', related_name='purchase_invoices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Facturi de Cumparare'
    
    def __str__(self):
        return self.supplier_name

# SalesInvoice model will have a many to one relationship
# with the User model via 'owner' foreign key
# related_name refers to a custom access name for the current model
class SalesInvoice(models.Model):
    type = models.CharField(max_length=100, blank=False, default='')
    invoice_number = models.CharField(max_length=15, blank=False, default='')
    invoice_series = models.CharField(max_length=15, blank=False, default='')
    client_code = models.CharField(max_length=5, blank=False, default='')
    client_name = models.CharField(max_length=255, blank=False, default='')
    client_vat = models.BooleanField(blank=False, default=False)
    invoice_date = models.DateField(blank=False, default='')
    invoice_due_date = models.DateField(blank=False, default='')
    invoice_gross_value = models.IntegerField(blank=False, default=0)
    invoice_vat_value = models.IntegerField(blank=False, default=0)
    invoice_net_value = models.IntegerField(blank=False, default=0)
    owner = models.ForeignKey('auth.User', related_name='sales_invoices', on_delete=models.CASCADE)
    created_at = models.DateTimeField(blank=True, default=datetime.now())
    updated_at = models.DateTimeField(blank=True, default=datetime.now())

    class Meta:
        ordering = ['created_at']
        verbose_name_plural = 'Facturi de Vanzare'
    
    def __str__(self):
        return self.client_name