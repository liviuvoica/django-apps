from rest_framework import generics, permissions
from contact_api import serializers
from django.contrib.auth.models import User
from error_and_notification_api.models import ErrorAndNotification
from error_and_notification_api.permissions import IsOwnerOrReadOnly

# Create your views here.

# Provide a read-only endpoint to represent a list of all blog categories
# ListAPIView used for read-only endpoint to represent a collection of model instance
# ListAPIView provides a GET method handler
class ErrorAndNotificationList(generics.ListCreateAPIView):
    queryset = ErrorAndNotification.objects.all()
    serializer_class = serializers.ErrorAndNotificationSerializer
    # Let unauthenticated users to only read the blog posts
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    # This function will set the blog post owner to the current user
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Provide a read-write-delete endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView used for read-write-only endpoint to represent a single model instance
# RetrieveUpdateDestroyAPIView provides GET, PUT, PATCH and DELETE method handler
class ErrorAndNotificationListDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ErrorAndNotification.objects.all()
    serializer_class = serializers.ErrorAndNotificationSerializer
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