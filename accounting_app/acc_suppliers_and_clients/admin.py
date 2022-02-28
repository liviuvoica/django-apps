from django.contrib import admin
from acc_suppliers_and_clients.models import Supplier
from acc_suppliers_and_clients.models import Client

# Register your models here.

class SupplierAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_name',
        'get_trade_register_registration_number',
        'get_fiscal_code',
        'get_analytical_account',
        'get_county',
        'get_city',
        'get_address',
        'get_phone_number',
        'get_email_address'
    )
    
    def get_name(self, obj):
        return str(obj.name).upper()
    get_name.short_description = "Denumire client"
    
    def get_trade_register_registration_number(self, obj):
        return str(obj.trade_register_registration_number).upper()
    get_trade_register_registration_number.short_description = "Nr Registrul Comertului"
    
    def get_fiscal_code(self, obj):
        return str(obj.fiscal_code).upper()
    get_fiscal_code.short_description = "Cod Fiscal"
    
    def get_analytical_account(self, obj):
        return str(obj.analytical_account).upper()
    get_analytical_account.short_description = "Cont contabil"
    
    def get_county(self, obj):
        return str(obj.county).upper()
    get_county.short_description = "Judet"
    
    def get_city(self, obj):
        return str(obj.city).upper()
    get_city.short_description = "Oras"
    
    def get_address(self, obj):
        return str(obj.address).upper()
    get_address.short_description = "Adresa"
    
    def get_phone_number(self, obj):
        return str(obj.phone_number).upper()
    get_phone_number.short_description = "Numar de telefon"
    
    def get_email_address(self, obj):
        return str(obj.email_address).upper()
    get_email_address.short_description = "Adresa de email"

class ClientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_name',
        'get_trade_register_registration_number',
        'get_fiscal_code',
        'get_pin',
        'get_analytical_account',
        'get_county',
        'get_city',
        'get_address',
        'get_phone_number',
        'get_email_address'
    )
    
    def get_name(self, obj):
        return str(obj.name).upper()
    get_name.short_description = "Denumire client"
    
    def get_trade_register_registration_number(self, obj):
        return str(obj.trade_register_registration_number).upper()
    get_trade_register_registration_number.short_description = "Nr Registrul Comertului"
    
    def get_fiscal_code(self, obj):
        return str(obj.fiscal_code).upper()
    get_fiscal_code.short_description = "Cod Fiscal"
    
    def get_pin(self, obj):
        return str(obj.pin).upper()
    get_pin.short_description = "CNP"
    
    def get_analytical_account(self, obj):
        return str(obj.analytical_account).upper()
    get_analytical_account.short_description = "Cont contabil"
    
    def get_county(self, obj):
        return str(obj.county).upper()
    get_county.short_description = "Judet"
    
    def get_city(self, obj):
        return str(obj.city).upper()
    get_city.short_description = "Oras"
    
    def get_address(self, obj):
        return str(obj.address).upper()
    get_address.short_description = "Adresa"
    
    def get_phone_number(self, obj):
        return str(obj.phone_number).upper()
    get_phone_number.short_description = "Numar de telefon"
    
    def get_email_address(self, obj):
        return str(obj.email_address).upper()
    get_email_address.short_description = "Adresa de email"

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Client, ClientAdmin)