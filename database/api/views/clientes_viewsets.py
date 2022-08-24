from rest_framework import viewsets, permissions

from database.models import Cliente
from database.api.serializers import ClienteSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.using("homebanking").all()
    serializer_class = ClienteSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
