from rest_framework import permissions


class OwnerOrReadOnly(permissions.BasePermission):
    """Permission для создателей объекта."""

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.owner == request.user)
