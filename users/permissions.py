from rest_framework.permissions import BasePermission

from users.models import User


class IsOwner(BasePermission):
    """Разрешение: доступ только для владельца объекта."""

    def has_object_permission(self, request, view, obj):
        if isinstance(obj, User):
            return obj == request.user


class IsSuperuser(BasePermission):
    """Разрешение: доступ только для суперпользователя."""

    def has_permission(self, request, view):
        return request.user.is_superuser
