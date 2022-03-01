from rest_framework import generics, permissions
from acc_operations import serializers
from django.contrib.auth.models import User
from acc_operations.models import PurchaseInvoice
from acc_operations.models import SalesInvoice
from acc_operations.permissions import IsOwnerOrReadOnly

# Create your views here.

# Provide a read-only endpoint to represent the list of all purchase invoices
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class PurchaseInvoiceList(generics.ListCreateAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = serializers.PurchaseInvoiceSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class PurchaseInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseInvoice.objects.all()
    serializer_class = serializers.PurchaseInvoiceSerializer
    # Let authenticated users to only read blog posts that they do not own, but do not let them to edit or delete them
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

# Provide a read-only endpoint to represent the list of all sales invoices
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class SalesInvoiceList(generics.ListCreateAPIView):
    queryset = SalesInvoice.objects.all()
    serializer_class = serializers.SalesInvoiceSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class SalesInvoiceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SalesInvoice.objects.all()
    serializer_class = serializers.SalesInvoiceSerializer
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