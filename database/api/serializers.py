from rest_framework import serializers

from database.models import Cliente, Cuenta, Direcciones, Prestamo, Sucursal, Tarjeta


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = [
            "customer_id",
            "customer_name",
            "customer_surname",
            "customer_dni",
            "dob",
            "branch_id",
        ]


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cuenta
        fields = "__all__"


# FloatField(source="sucursal.branch_id", read_only=True)
class PrestamoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prestamo
        fields = [
            "loan_id",
            "loan_type",
            "loan_date",
            "loan_total",
            "customer_id",
        ]

    def create(self, validated_data):
        return Prestamo.objects.using("homebanking").create(**validated_data)


class SucursalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sucursal
        fields = "__all__"


class TarjetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarjeta
        fields = [
            "tarjeta_id",
            "numero_tarjeta",
            "cvv",
            "fecha_creacion",
            "fecha_vencimiento",
            "tipo_tarjeta",
            "cliente_id",
        ]


class DireccionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direcciones
        fields = [
            "titular_id",

            "calle",
            "numero",
            "ciudad",
            "provincia",
            "pais",
        ]