from rest_framework import viewsets, permissions
from rest_framework.response import Response


from database.models import Cliente, Prestamo, Sucursal
from database.api.serializers import PrestamoSerializer, SucursalSerializer
from database.api.permissions import GetOwnData


class PrestamosViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.using("homebanking").all()
    serializer_class = PrestamoSerializer

    # Permisos segun solicitud
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated, GetOwnData]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    # Listado dinamico según rol del usuario
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
        return Response(
            {"message": "no se encuentran préstamos del cliente solicitado."}
        )


class SucursalPrestamosViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Sucursal.objects.using("homebanking").all()
    serializer_class = SucursalSerializer

    # Permisos segun solicitud
    def get_permissions(self):
        if self.action == "list":
            permission_classes = [permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]

    # metodo para vista prestamos por sucursal
    def retrieve(self, request, pk, *args, **kwargs):
        clientes = Cliente.objects.using("homebanking").filter(branch_id=pk)
        prestamos = []
        for cliente in clientes:
            prestamos += Prestamo.objects.using("homebanking").filter(
                customer_id=cliente.customer_id
            )

        if prestamos:
            serializer = PrestamoSerializer(prestamos, many=True)
            return Response(serializer.data)
        return Response({"message": "Sucursal sin prestamos registrados"})
