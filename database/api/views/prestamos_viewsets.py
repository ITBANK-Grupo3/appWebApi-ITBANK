from urllib import request
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from database.models import Cliente, Prestamo, Sucursal, Cuenta
from database.api.serializers import PrestamoSerializer, SucursalSerializer
from database.api.permissions import GetOwnData


class PrestamosViewSet(viewsets.ModelViewSet):
    # Asignacion del modelo
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

    # Listar según filtro
    def list(self, request, *args, **kwargs):
        if "sucursal_id" in self.request.GET:
            sucursal = int(self.request.GET["sucursal_id"])
            clientes = Cliente.objects.using("homebanking").filter(branch_id=sucursal)
            data = []
            for cliente in clientes:
                data += Prestamo.objects.using("homebanking").filter(
                    customer_id=cliente.customer_id
                )
        else:
            data = self.filter_queryset(self.get_queryset())
        if data:
            serializer = self.get_serializer(data, many=True)
            return Response(serializer.data)
        return Response(
            {"message": "La sucursal solicitada no posee prestamos actualmente"}
        )

    # Modificamos el post
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            # Cambiamos el estado de la cuenta al subir un prestamo
            cuenta_cliente = (
                Cuenta.objects.using("homebanking")
                .filter(customer_id=request.data["customer_id"])
                .filter(tipo_cuenta=1)
                .first()
            )
            cuenta_cliente.balance += request.data["loan_total"]
            cuenta_cliente.save()

            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Cancelacion de prestamo
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        # Restamos el monto de la cuenta
        cuenta_cliente = (
            Cuenta.objects.using("homebanking")
            .filter(customer_id=instance.customer_id)
            .filter(tipo_cuenta=1)
            .first()
        )
        cuenta_cliente.balance -= instance.loan_total
        cuenta_cliente.save()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)


class SucursalViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.using("homebanking").all()
    serializer_class = SucursalSerializer
