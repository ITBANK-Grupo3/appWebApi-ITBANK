from rest_framework import viewsets, permissions
from rest_framework.response import Response

from database.models import Cliente, Cuenta
from database.api.serializers import ClienteSerializer, AccountSerializer
from database.api.permissions import GetOwnData


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.using("homebanking").all()
    serializer_class = ClienteSerializer

    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


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
        if request.user.is_staff == 1:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            cliente_dni = request.user.username
            cliente_id = (
                Cliente.objects.using("homebanking")
                .filter(customer_dni=cliente_dni)
                .first()
                .customer_id
            )
            queryset = Cuenta.objects.using("homebanking").filter(
                customer_id=cliente_id
            )

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
