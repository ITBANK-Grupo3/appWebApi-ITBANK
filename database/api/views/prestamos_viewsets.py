from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from database.models import Cliente, Prestamo, Sucursal
from database.api.serializers import PrestamoSerializer, SucursalSerializer
from database.api.permissions import GetOwnData


class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.using("homebanking").all()
    serializer_class = PrestamoSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["customer_id"]

    # Permisos segun solicitud
    def get_permissions(self):
        if self.action == "retrieve":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]


class SucursalPrestamosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.using("homebanking").all()
    serializer_class = SucursalSerializer
