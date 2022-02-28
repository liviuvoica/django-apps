from django.contrib import admin
from acc_suppliers_and_clients.models import Supplier
from acc_suppliers_and_clients.models import Client

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'trade_register_registration_number',
        'fiscal_code',
        'analytical_account',
        'county',
        'city',
        'address',
        'bank_account',
        'bank_name',
        'phone_number',
        'email_address',
        'get_owner',
        'created_at',
        'updated_at'
    )
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'trade_register_registration_number',
        'fiscal_code',
        'pin',
        'analytical_account',
        'county',
        'city',
        'address',
        'bank_account',
        'bank_name',
        'phone_number',
        'email_address',
        'get_owner',
        'created_at',
        'updated_at'
    )
    
    def get_owner(self, obj):
        return str(obj.owner).upper()
    get_owner.short_description = "owner"

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Client, ClientAdmin)