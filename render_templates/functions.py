from database import models as models_db
import tarjetas


def get_user_info(dni):
    """
    Funcion que retorna la informacion almacenada relevante del
    usuario

    args: dni (entero)

    return: diccionario con los datos del usuario
    """
    # Obtenemos los datos del cliente
    cliente = models_db.Cliente.objects.using("homebanking").filter(customer_dni=dni)

    diccionario = {}

    if len(cliente) > 0:
        customer_id = cliente[0].customer_id

        # Recoleccion datos de las diferentes cuentas
        caja_pesos = (
            models_db.Cuenta.objects.using("homebanking")
            .filter(customer_id=customer_id)
            .filter(tipo_cuenta=1)
        )

        diccionario = {
            "customer_id": customer_id,
            "caja_pesos": caja_pesos[0],
        }

        # Buscar cuenta segun tipo de cliente
        if cliente[0].tipo_cliente == 2 or cliente[0].tipo_cliente == 3:
            caja_dolares = (
                models_db.Cuenta.objects.using("homebanking")
                .filter(customer_id=customer_id)
                .filter(tipo_cuenta=2)
            )
            cuenta_corriente = (
                models_db.Cuenta.objects.using("homebanking")
                .filter(customer_id=customer_id)
                .filter(tipo_cuenta=3)
            )
            # Cargamos las cuentas en el diccionario
            diccionario["caja_dolares"] = caja_dolares[0]
            diccionario["cuenta_corriente"]: cuenta_corriente[0]

        # Recopilamos datos de las tarjetas a su nombre
        tarjetas = models_db.Tarjeta.objects.using("homebanking").filter(
            cliente_id=customer_id
        )
        if len(tarjetas) > 0:
            diccionario["tarjetas"] = tarjetas

    return diccionario
