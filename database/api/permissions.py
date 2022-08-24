from rest_framework import permissions


class GetOwnData(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.customer_dni == request.user.username or request.user.is_staff == 1
