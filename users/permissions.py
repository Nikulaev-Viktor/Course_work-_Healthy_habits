from rest_framework import permissions


class IsOwnerOrSuperUser(permissions.BasePermission):
    """Проверка на владельца или суперпользователя"""

    def has_object_permission(self, request, view, obj):
        return request.user == obj or request.user.is_superuser

