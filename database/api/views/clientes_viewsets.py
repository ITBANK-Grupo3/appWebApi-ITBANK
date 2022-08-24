from rest_framework import viewsets, permissions

from database.models import Cliente
from database.api.serializers import ClienteSerializer
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
