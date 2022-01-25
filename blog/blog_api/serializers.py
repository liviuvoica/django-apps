from asyncio.windows_events import NULL
from turtle import title
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User
from blog_api.models import Post
from blog_api.models import Comment
from blog_api.models import Category


# CategorySerializer class will inherit properties and methods from the ModelSerializer class
class CategorySerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Category
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'name',
            'owner',
            'posts'
        ]

# PostSerializer class will inherit properties and methods from the ModelSerializer class
class PostSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        # Define the model that should be associated with this serializer
        model = Post
        # Indicates which fields from the model should be included in the serializer
        fields = [
            'id',
            'title',
            'body',
            'owner',
            'comments'
        ]

    # Validate the Post title that the user sends via the API endpoint
    def validate_title(self, post_title):
        # Check if the inserted title contains numbers
        if post_title == '':
            raise ValidationError("You did not inserted anything in the title field! Please try again!")
        if post_title.isdigit() == True:
            raise ValidationError("The post title you have inserted ('" + post_title + "') must only contain letters! Please try again!")
        if len(post_title) <= 10:
            raise ValidationError("The post title you have inserted ('" + post_title + "') is too short! It must have a minimum of 10 characters! Please try again!")

# CommentSerializer class will inherit properties and methods from the ModelSerializer class
class CommentSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Comment
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'body',
            'owner',
            'post'
        ]

# UserSerializer class will inherit properties and methods from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    # Define the primary key for the current model
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
            'posts',
            'comments'
        ]