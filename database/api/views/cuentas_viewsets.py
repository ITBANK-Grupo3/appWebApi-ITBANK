from rest_framework import viewsets, permissions
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from database.models import Cliente, Cuenta
from database.api.serializers import AccountSerializer
from database.api.permissions import GetOwnData


class CuentaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Cuenta.objects.using("homebanking").all()
    serializer_class = AccountSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["customer_id"]

    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
