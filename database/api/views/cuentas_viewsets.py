from rest_framework import viewsets, permissions
from rest_framework.response import Response

from database.models import Cliente, Cuenta
from database.api.serializers import AccountSerializer
from database.api.permissions import GetOwnData


class CuentaViewSet(viewsets.ModelViewSet):
    queryset = Cuenta.objects.using("homebanking").all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        # comprobamos rol del usuario
        if not request.user.is_staff == 1:
            dni = request.user.username
            cliente_id = (
                Cliente.objects.using("homebanking").filter(customer_dni=dni).first()
            )
            queryset = self.queryset.filter(customer_id=cliente_id.customer_id)
        else:
            queryset = self.get_queryset()

        serializer = self.get_serializer(queryset, many=True)
        if serializer.data:
            return Response(serializer.data)
        return Response({"message": "no se encuentran cuentas del cliente solicitado."})
