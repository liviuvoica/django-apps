from asyncio.windows_events import NULL
from turtle import title
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

from newsletter_api.models import Newsletter


# NewsletterSerializer class will inherit properties and methods from the ModelSerializer class
class NewsletterSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Newsletter
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'full_name',
            'email',
            'privacy_policy',
            'owner',
        ]

# UserSerializer class will inherit properties and methods from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    # Define the primary key for the current model
    messages = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
            'subscribers',
        ]