from rest_framework import serializers

from database.models import Cliente, Cuenta


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
