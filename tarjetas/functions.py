import random
import datetime
from database import models as models_db


fecha_actual = datetime.date.today()
fecha_formateada = datetime.date.strftime(fecha_actual, "%m/%y")

fechita = fecha_actual.strftime("%m")
fecha_vencimiento = f"{fechita}/{fecha_actual.year + 5 - 2000}"


def generate_card_for_user(cliente_id):
    models_db.Tarjeta.objects.using("homebanking").create(
        numero_tarjeta=f"5104{random.randint(100000000000,999999999999)}",
        cvv=random.randint(100, 999),
        fecha_creacion=fecha_formateada,
        fecha_vencimiento=fecha_vencimiento,
        tipo_tarjeta="debito",
        cliente_id=cliente_id,
        marca_tarjeta_id=2,
    )
