from asyncio.windows_events import NULL
from turtle import title
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

from acc_suppliers_and_clients.models import Supplier
from acc_suppliers_and_clients.models import Client
from acc_suppliers_and_clients.models import ChartOfAccount


# SupplierSerializer class will inherit properties and methods from the ModelSerializer class
class SupplierSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Supplier
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
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
            'owner',
        ]


# ClientSerializer class will inherit properties and methods from the ModelSerializer class
class ClientSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Client
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
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
            'owner',
        ]


# ChartOfAccountSerializer class will inherit properties and methods from the ModelSerializer class
class ChartOfAccountSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = ChartOfAccount
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'account',
            'name',
            'type',
            'is_active',
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
            'suppliers',
            'clients',
            'chart_of_accounts',
        ]