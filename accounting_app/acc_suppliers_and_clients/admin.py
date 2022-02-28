from django.contrib import admin
from acc_suppliers_and_clients.models import Supplier
from acc_suppliers_and_clients.models import Client
from acc_suppliers_and_clients.models import ChartOfAccount
from acc_suppliers_and_clients.models import Article

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

class ChartOfAccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_account',
        'get_name',
        'get_type',
        'get_is_active'
    )
    
    def get_account(self, obj):
        return str(obj.account).upper()
    get_account.short_description = "Cont contabil"
    
    def get_name(self, obj):
        return str(obj.name).upper()
    get_name.short_description = "Denumire cont contabil"
    
    def get_type(self, obj):
        return str(obj.type).upper()
    get_type.short_description = "Tip cont contabil"
    
    def get_is_active(self, obj):
        return str(obj.is_active).upper()
    get_is_active.short_description = "Blocat?"

class ArticleAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'get_code',
        'get_name',
        'get_um',
        'get_vat',
        'get_type',
        'get_current_stock',
        'get_sales_price',
        'get_sales_price_vat',
    )
    
    def get_code(self, obj):
        return str(obj.code).upper()
    get_code.short_description = "Cod articol"
    
    def get_name(self, obj):
        return str(obj.name).upper()
    get_name.short_description = "Denumire articol"
    
    def get_um(self, obj):
        return str(obj.um).upper()
    get_um.short_description = "Unitate de masura"
    
    def get_vat(self, obj):
        return str(obj.vat).upper()
    get_vat.short_description = "TVA %"
    
    def get_type(self, obj):
        return str(obj.type).upper()
    get_type.short_description = "Tip articol"
    
    def get_current_stock(self, obj):
        return str(obj.current_stock).upper()
    get_current_stock.short_description = "Stoc current"
    
    def get_sales_price(self, obj):
        return str(obj.sales_price).upper()
    get_sales_price.short_description = "Pret de vanzare"
    
    def get_sales_price_vat(self, obj):
        return str(obj.sales_price_Vat).upper()
    get_sales_price_vat.short_description = "Pret de vanzare cu TVA"

admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(ChartOfAccount, ChartOfAccountAdmin)
admin.site.register(Article, ArticleAdmin)