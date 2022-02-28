from rest_framework import generics, permissions
from acc_suppliers_and_clients import serializers
from django.contrib.auth.models import User
from acc_suppliers_and_clients.models import Supplier
from acc_suppliers_and_clients.models import Client
from acc_suppliers_and_clients.models import ChartOfAccount
from acc_suppliers_and_clients.models import Article
from acc_suppliers_and_clients.permissions import IsOwnerOrReadOnly

# Create your views here.

# Provide a read-only endpoint to represent the list of all suppliers
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class SupplierList(generics.ListCreateAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class SupplierDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Supplier.objects.all()
    serializer_class = serializers.SupplierSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent the list of all clients
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class ClientList(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class ClientDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent the list of all chart of accounts
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class ChartOfAccountList(generics.ListCreateAPIView):
    queryset = ChartOfAccount.objects.all()
    serializer_class = serializers.ChartOfAccountSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class ChartOfAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ChartOfAccount.objects.all()
    serializer_class = serializers.ChartOfAccountSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent the list of all articles
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