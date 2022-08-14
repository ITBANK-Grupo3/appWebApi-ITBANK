import random
from database import models as models_db


def crear_cuentas(tipo_cliente, id):
    if int(tipo_cliente) == 1:
        # Caja de ahorro en pesos
        models_db.Cuenta.objects.using("homebanking").create(
            customer_id=id,
            balance=0,
            iban=f"AR052004000000{random.randint(1000000000,9999999999)}",
            tipo_cuenta=1,
        )
    elif int(tipo_cliente) == 2 or int(tipo_cliente) == 3:
        # Caja de ahorro en pesos
        models_db.Cuenta.objects.using("homebanking").create(
            customer_id=id,
            balance=0,
            iban=f"AR052004000000{random.randint(1000000000,9999999999)}",
            tipo_cuenta=1,
        )
        # Caja de ahorro en dolares
        models_db.Cuenta.objects.using("homebanking").create(
            customer_id=id,
            balance=0,
            iban=f"AR052004000000{random.randint(1000000000,9999999999)}",
            tipo_cuenta=2,
        )
        # Cuenta corriente en pesos
        models_db.Cuenta.objects.using("homebanking").create(
            customer_id=id,
            balance=0,
            iban=f"AR052004000000{random.randint(1000000000,9999999999)}",
            tipo_cuenta=3,
        )
