from rest_framework import viewsets, permissions
from rest_framework.response import Response

from database.models import Cliente, Tarjeta
from database.api.serializers import TarjetaSerializer
from database.api.permissions import GetOwnData


class TarjetaViewSet(viewsets.ModelViewSet):
    queryset = Tarjeta.objects.using("homebanking").all()
    serializer_class = TarjetaSerializer
    permission_classes = [permissions.IsAdminUser]

    # ver tarjetas por id del cliente
    def retrieve(self, request, pk, *args, **kwargs):
        tarjetas = Tarjeta.objects.using("homebanking").filter(cliente_id=pk)
        if tarjetas:
            serializer = TarjetaSerializer(tarjetas, many=True)
            return Response(serializer.data)
        return Response({"message": "El cliente no posee tarjetas a su nombre."})
