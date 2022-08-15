from database import models as db_models


def solicitar_prestamo(dni, monto, tipo_prestamo, fecha_inicio):
    """Funcion para cargar y ejecutar el prestamo"""

    # Buscamos la información del cliente
    cliente = cliente = db_models.Cliente.objects.using("homebanking").filter(
        customer_dni=dni
    )

    monto = int(monto)

    # condicional de cliente encontrado
    if len(cliente) > 0:
        # Datos del cliente
        customer_id = cliente[0].customer_id
        tipo_cliente = cliente[0].tipo_cliente

        # Condicionales según cuenta
        if tipo_cliente.tipo_id == 1:
            if monto <= 100000:
                caja_pesos = (
                    db_models.Cuenta.objects.using("homebanking")
                    .filter(customer_id=customer_id)
                    .filter(tipo_cuenta=1)
                )
                caja_pesos = caja_pesos[0]
                caja_pesos.balance += monto
                caja_pesos.save()
                return True
            else:
                return False
        elif tipo_cliente.tipo_id == 2:
            if monto <= 300000:
                caja_pesos = (
                    db_models.Cuenta.objects.using("homebanking")
                    .filter(customer_id=customer_id)
                    .filter(tipo_cuenta=1)
                )
                caja_pesos = caja_pesos[0]
                caja_pesos.balance += monto
                caja_pesos.save()
                return True
            else:
                return False

        elif tipo_cliente.tipo_id == 3:
            if monto <= 500000:
                caja_pesos = (
                    db_models.Cuenta.objects.using("homebanking")
                    .filter(customer_id=customer_id)
                    .filter(tipo_cuenta=1)
                )
                caja_pesos = caja_pesos[0]
                caja_pesos.balance += monto
                caja_pesos.save()
                return True
            else:
                return False
