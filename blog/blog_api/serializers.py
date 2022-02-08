from asyncio.windows_events import NULL
from turtle import title
from django.forms import ValidationError
from rest_framework import serializers
from django.contrib.auth.models import User

from blog_api.models import Category
from blog_api.models import Subcategory
from blog_api.models import Article
from blog_api.models import Comment


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
            'blog_category_title',
            'blog_category_short_description',
            'blog_category_description',
            'blog_category_is_active',
            'blog_image_card_url',
            'blog_category_path',
            'owner',
            'subcategories'
        ]

# CategorySerializer class will inherit properties and methods from the ModelSerializer class
class SubcategorySerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Subcategory
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'blog_category_id',
            'blog_subcategory_title',
            'blog_subcategory_short_description',
            'blog_subcategory_description',
            'blog_subcategory_is_active',
            'blog_subcategory_path',
            'owner'
        ]

# CategorySerializer class will inherit properties and methods from the ModelSerializer class
class ArticleSerializer(serializers.ModelSerializer):
    # Define the foreign key for the current model
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        # Define the model that should be associated with this serializer
        model = Article
        # Indicates which fields from the model should be included in the serializer
        # In this way, the post field has write access by default. When a user creates a new comment, they also see the post it belongs to.
        fields = [
            'id',
            'blog_subcategory_id',
            'blog_article_author',
            'blog_article_time',
            'blog_article_title',
            'blog_article_short_description',
            'blog_article_content',
            'blog_article_path',
            'blog_article_is_active',
            'blog_article_rating_system',
            'blog_article_likes',
            'blog_article_dislikes',
            'owner'
        ]

# CategorySerializer class will inherit properties and methods from the ModelSerializer class
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
            'blog_article_id',
            'full_name',
            'email',
            'comment',
            'comment_is_public',
            'privacy_policy',
            'owner'
        ]

# UserSerializer class will inherit properties and methods from the ModelSerializer class
class UserSerializer(serializers.ModelSerializer):
    # Define the primary key for the current model
    categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    subcategories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    articles = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
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
            'categories',
            'subcategories',
            'articles',
            'comments'
        ]