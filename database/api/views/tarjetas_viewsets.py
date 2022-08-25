from rest_framework import viewsets, permissions
from rest_framework.response import Response

from database.models import Cliente, Tarjeta
from database.api.serializers import TarjetaSerializer
from database.api.permissions import GetOwnData


class TarjetaViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tarjeta.objects.using("homebanking").all()
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAdminUser]
