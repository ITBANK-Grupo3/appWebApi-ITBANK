from rest_framework import viewsets, permissions
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from database.models import Cuenta
from database.api.serializers import AccountSerializer
from database.api.permissions import GetOwnData
from .methods import CustomMethods


class CuentaViewSet(viewsets.ReadOnlyModelViewSet, CustomMethods):
    queryset = Cuenta.objects.using("homebanking").all()
    serializer_class = AccountSerializer

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["customer_id"]

    @method_decorator(csrf_exempt)
    def dispatch(self, request,  *args, **kwargs):
        return super().dispatch(request,  *args, **kwargs)

    def get_permissions(self):
        if self.action == "retrieve" or self.action == "list":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    def list(self, request, *args, **kwargs):
        # Cuentas del cliente
        if not request.user.is_staff == 1:
            cliente_id = self.get_customer_id(self.request)
            data = self.queryset.filter(customer_id=cliente_id) or [
                {"message": "El usuario solicitado no posee cuentas actualmente"}
            ]
        # Cuentas para staff
        else:
            data = self.filter_queryset(self.get_queryset())

        # corroboramos si llegó informacion
        if len(data) > 0 and type(data[0]) == dict:
            return Response(data)
        else:
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
