from asyncio.windows_events import NULL
from turtle import title
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

from acc_operations.models import PurchaseInvoice
from acc_operations.models import SalesInvoice


# PurchaseInvoiceSerializer class will inherit properties and methods from the ModelSerializer class
class PurchaseInvoiceSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = PurchaseInvoice
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'type',
            'invoice_number',
            'invoice_series',
            'supplier_code',
            'supplier_name',
            'supplier_vat',
            'invoice_date',
            'invoice_due_date',
            'invoice_gross_value',
            'invoice_vat_value',
            'invoice_net_value',
            'owner',
        ]


# SalesInvoiceSerializer class will inherit properties and methods from the ModelSerializer class
class SalesInvoiceSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = SalesInvoice
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'type',
            'invoice_number',
            'invoice_series',
            'client_code',
            'client_name',
            'client_vat',
            'invoice_date',
            'invoice_due_date',
            'invoice_gross_value',
            'invoice_vat_value',
            'invoice_net_value',
            'owner',
        ]


# UserSerializer class will inherit properties and methods from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    # Define the primary key for the current model
    suppliers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    clients = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # Define the model that should be associated with this serializer
        model = User
        # Indicates which fields from the model should be included in the serializer
        fields = [
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'purchase_invoices',
            'sales_invoices',
        ]