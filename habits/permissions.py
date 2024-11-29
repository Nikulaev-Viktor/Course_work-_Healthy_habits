from rest_framework import permissions


class IsOwner(permissions.BasePermission):
    """Проверка на владельца привычки."""
    def has_object_permission(self, request, view, obj):
        if obj.user == request.user:
            return True
        else:
            return False
