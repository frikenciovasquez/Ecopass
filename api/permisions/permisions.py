from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to do actions.
    """

    def has_object_permission(self, request, view, obj):
        # Permissions are only allowed to the owner of the device.
        return obj.user == request.user