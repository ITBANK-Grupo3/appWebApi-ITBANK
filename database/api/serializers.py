from rest_framework import serializers

from database.models import Cliente, Cuenta, Prestamo, Sucursal, Tarjeta


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
        fields = "__all__"

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
