from rest_framework import permissions

from database.models import Cliente


class GetOwnData(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user.is_staff == 1:
            dni = request.user.username
            cliente_id = (
                Cliente.objects.using("homebanking").filter(customer_dni=dni).first()
            )
            return obj.customer_id == cliente_id.customer_id
        return True
