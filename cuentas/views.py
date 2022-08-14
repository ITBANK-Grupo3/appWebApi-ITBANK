from django.shortcuts import render, redirect
from django.urls import reverse
from . import forms
from . import creacion_cuentas as cuentas
from tarjetas import functions as tarjetas
from database import models as models_db

# Create your views here.
def paquetes(request):
    form = forms.SelectorForm
    if request.method == "POST":
        form = form(data=request.POST)

        if form.is_valid():
            # Tipo Cliente solicitado
            tipo_cliente_id = request.POST.get("tipo_cliente", "")

            # recuperamos el último cliente
            cliente_id = (
                models_db.Cliente.objects.using("homebanking")
                .values("customer_id")
                .all()
                .last()
            )

            # Cargamos el tipo de cliente seleccionado
            models_db.Cliente.objects.using("homebanking").filter(
                customer_id=cliente_id["customer_id"]
            ).update(tipo_cliente=tipo_cliente_id)

            # creamos las cuentas segun corresponda
            cuentas.crear_cuentas(tipo_cliente_id, cliente_id["customer_id"])

            # generamos la tarjeta de debito inicial
            tarjetas.generate_card_for_user(cliente_id["customer_id"])
            # Redirigimos al login
            return redirect(reverse("login"))
    return render(request, "cuentas/paquetes.html", {"form": form})
