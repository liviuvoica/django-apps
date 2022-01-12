from django.contrib.auth.models import User, Group
from rest_framework import serializers

# Map the User model to the UserSerializer class
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# Map the Group model to the GroupSerializer class
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

# Map the Customer model to the CustomerSerializer class
class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['url', 'name']