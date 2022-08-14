# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditoriaCuenta(models.Model):
    old_id = models.AutoField(primary_key=True)
    new_id = models.IntegerField()
    old_balance = models.IntegerField()
    new_balance = models.IntegerField()
    old_iban = models.IntegerField()
    new_iban = models.IntegerField()
    old_type = models.TextField()  # This field type is a guess.
    new_type = models.TextField()  # This field type is a guess.
    user_action = models.TextField()  # This field type is a guess.
    created_at = models.TextField()

    class Meta:
        managed = False
        db_table = "auditoria_cuenta"


class CorrespondenciaDirecciones(models.Model):
    correspondencia_id = models.AutoField(primary_key=True, blank=True, null=False)
    tipo = models.TextField()

    class Meta:
        managed = False
        db_table = "correspondencia_direcciones"


class Cuenta(models.Model):
    account_id = models.AutoField(primary_key=True)
    customer_id = models.IntegerField()
    balance = models.IntegerField()
    iban = models.TextField()
    tipo_cuenta = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = "cuenta"


class Direcciones(models.Model):
    dire_id = models.AutoField(primary_key=True)
    correspondencia = models.ForeignKey(CorrespondenciaDirecciones, models.DO_NOTHING)
    titular_id = models.IntegerField()
    calle = models.TextField()
    numero = models.IntegerField()
    ciudad = models.TextField()
    provincia = models.TextField()
    pais = models.TextField()

    class Meta:
        managed = False
        db_table = "direcciones"


class Empleado(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.TextField()
    employee_surname = models.TextField()
    employee_hire_date = models.TextField()
    employee_dni = models.TextField(
        db_column="employee_DNI"
    )  # Field name made lowercase.
    branch_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "empleado"


class MarcaTarjeta(models.Model):
    marca_tarjeta_id = models.AutoField(primary_key=True)
    marca_tarjeta_nombre = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "marca_tarjeta"


class Movimientos(models.Model):
    transaction_id = models.AutoField(primary_key=True)
    emisor_id = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name="emisor"
    )
    receptor_id = models.ForeignKey(
        Cuenta, on_delete=models.CASCADE, related_name="receptor"
    )
    amount = models.FloatField()
    type = models.CharField(max_length=50)
    created_at = models.DateField()

    class Meta:
        managed = False
        db_table = "movimientos"


class Prestamo(models.Model):
    loan_id = models.AutoField(primary_key=True)
    loan_type = models.TextField()
    loan_date = models.TextField()
    loan_total = models.IntegerField()
    customer_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "prestamo"


class Sucursal(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_number = models.BinaryField()
    branch_name = models.TextField()
    branch_address_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = "sucursal"


class Tarjeta(models.Model):
    tarjeta_id = models.AutoField(primary_key=True)
    numero_tarjeta = models.CharField(unique=True, max_length=16)
    cvv = models.TextField()  # This field type is a guess.
    fecha_creacion = models.TextField()
    fecha_vencimiento = models.TextField()
    tipo_tarjeta = models.TextField()  # This field type is a guess.
    cliente_id = models.IntegerField()
    marca_tarjeta = models.ForeignKey(MarcaTarjeta, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = "tarjeta"


class TipoCliente(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    nombre_tipo = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "tipo_cliente"


class TipoCuenta(models.Model):
    tipo_id = models.AutoField(primary_key=True)
    nombre_tipo = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = "tipo_cuenta"


class Cliente(models.Model):
    customer_id = models.AutoField(primary_key=True)
    customer_name = models.TextField()
    customer_surname = models.TextField()  # This field type is a guess.
    customer_dni = models.TextField(
        db_column="customer_DNI"
    )  # Field name made lowercase.
    dob = models.TextField(blank=True, null=True)
    branch_id = models.IntegerField()
    tipo_cliente = models.ForeignKey(
        "TipoCuenta", models.DO_NOTHING, db_column="tipo_cliente", blank=True, null=True
    )

    class Meta:
        managed = False
        db_table = "cliente"
