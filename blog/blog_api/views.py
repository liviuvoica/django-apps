from rest_framework import generics, permissions
from blog_api import serializers
from django.contrib.auth.models import User
from blog_api.models import Category
from blog_api.models import Subcategory
from blog_api.models import Article
from blog_api.models import Comment
from blog_api.permissions import IsOwnerOrReadOnly

# Create your views here.

# Provide a read-only endpoint to represent a list of all blog categories
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent a list of all blog categories
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class SubcategoryList(generics.ListCreateAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class SubcategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = serializers.SubcategorySerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent a list of all blog categories
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = serializers.ArticleSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent a list of all blog categories
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent a list of all users
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# Provide a read-only access via GET method to fetch a specific user
# RetrieveAPIView used for read-only endpoint to represent a single model instance
# RetrieveAPIView provides a GET method handler
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer