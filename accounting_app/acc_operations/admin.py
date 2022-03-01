from django.contrib import admin
from acc_operations.models import PurchaseInvoice
from acc_operations.models import SalesInvoice

# Register your models here.

class PurchaseInvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_type',
        'get_invoice_number',
        'get_invoice_series',
        'get_supplier_code',
        'get_supplier_name',
        'get_supplier_vat',
        'get_invoice_date',
        'get_invoice_due_date',
        'get_invoice_gross_value',
        'get_invoice_vat_value',
        'get_invoice_net_value'
    )
    
    def get_type(self, obj):
        return str(obj.type).upper()
    get_type.short_description = "Tip Doc."
    
    def get_invoice_number(self, obj):
        return str(obj.invoice_number).upper()
    get_invoice_number.short_description = "Nr. Intrare"
    
    def get_invoice_series(self, obj):
        return str(obj.invoice_series).upper()
    get_invoice_series.short_description = "Nr. Doc."
    
    def get_supplier_code(self, obj):
        return str(obj.supplier_code).upper()
    get_supplier_code.short_description = "Cod Furnizor"
    
    def get_supplier_name(self, obj):
        return str(obj.supplier_name).upper()
    get_supplier_name.short_description = "Denumire furnizor"
    
    def get_supplier_vat(self, obj):
        return str(obj.supplier_vat).upper()
    get_supplier_vat.short_description = "TVA la Incasare"
    
    def get_invoice_date(self, obj):
        return str(obj.invoice_date).upper()
    get_invoice_date.short_description = "Data factura"
    
    def get_invoice_due_date(self, obj):
        return str(obj.invoice_due_date).upper()
    get_invoice_due_date.short_description = "Data scadenta"
    
    def get_invoice_gross_value(self, obj):
        return str(obj.invoice_gross_value).upper()
    get_invoice_gross_value.short_description = "Valoare bruta"
    
    def get_invoice_vat_value(self, obj):
        return str(obj.invoice_vat_value).upper()
    get_invoice_vat_value.short_description = "Valoare TVA"
    
    def get_invoice_net_value(self, obj):
        return str(obj.invoice_net_value).upper()
    get_invoice_net_value.short_description = "Valoare neta"

class SalesInvoiceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_type',
        'get_invoice_number',
        'get_invoice_series',
        'get_client_code',
        'get_client_name',
        'get_client_vat',
        'get_invoice_date',
        'get_invoice_due_date',
        'get_invoice_gross_value',
        'get_invoice_vat_value',
        'get_invoice_net_value'
    )
    
    def get_type(self, obj):
        return str(obj.type).upper()
    get_type.short_description = "Tip Doc."
    
    def get_invoice_number(self, obj):
        return str(obj.invoice_number).upper()
    get_invoice_number.short_description = "Nr. Intrare"
    
    def get_invoice_series(self, obj):
        return str(obj.invoice_series).upper()
    get_invoice_series.short_description = "Nr. Doc."
    
    def get_client_code(self, obj):
        return str(obj.client_code).upper()
    get_client_code.short_description = "Cod Client"
    
    def get_client_name(self, obj):
        return str(obj.client_name).upper()
    get_client_name.short_description = "Denumire client"
    
    def get_client_vat(self, obj):
        return str(obj.client_vat).upper()
    get_client_vat.short_description = "TVA la Incasare"
    
    def get_invoice_date(self, obj):
        return str(obj.invoice_date).upper()
    get_invoice_date.short_description = "Data factura"
    
    def get_invoice_due_date(self, obj):
        return str(obj.invoice_due_date).upper()
    get_invoice_due_date.short_description = "Data scadenta"
    
    def get_invoice_gross_value(self, obj):
        return str(obj.invoice_gross_value).upper()
    get_invoice_gross_value.short_description = "Valoare bruta"
    
    def get_invoice_vat_value(self, obj):
        return str(obj.invoice_vat_value).upper()
    get_invoice_vat_value.short_description = "Valoare TVA"
    
    def get_invoice_net_value(self, obj):
        return str(obj.invoice_net_value).upper()
    get_invoice_net_value.short_description = "Valoare neta"

admin.site.register(PurchaseInvoice, PurchaseInvoiceAdmin)
admin.site.register(SalesInvoice, SalesInvoiceAdmin)