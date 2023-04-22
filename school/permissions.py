from rest_framework import permissions


class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.METHOD in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_superuser