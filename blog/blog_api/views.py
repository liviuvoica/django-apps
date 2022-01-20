from rest_framework import generics
from blog_api import serializers
from django.contrib.auth.models import User
from blog_api.models import Post
from blog_api.models import Comment
from blog_api.models import Category
from rest_framework import permissions
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

# Provide a read-only endpoint to represent a list of all blog posts
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent a list of all blog post comments
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