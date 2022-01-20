from rest_framework import permissions

# IsOwnerOrReadOnly will check if the requesting user is the owner of the given object
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user