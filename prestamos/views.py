from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import PrestamoForm
from render_templates.views import home
from database import models as db_models
from . import functions as pedido


# Create your views here.
@login_required(login_url="/home/")
def prestamo(request):
    # cliente = db_models.Cliente.objects.using('homebanking').all()
    # cuenta = db_models.Cuenta.objects.using('homebanking').all()
    prestamo_form = PrestamoForm
    if not request.user.is_authenticated:
        home(request)
    if request.method == "POST":
        prestamo_form = prestamo_form(data=request.POST)
        if prestamo_form.is_valid():
            # Datos recuperados
            monto = request.POST.get("monto", "")
            tipo_prestamo = request.POST.get("tipo_prestamo", "")
            fecha_inicio = request.POST.get("fecha_inicio", "")
            dni = request.user.username

            # Solicitud y creacion prestamo
            solicitud = pedido.solicitar_prestamo(
                dni, monto, tipo_prestamo, fecha_inicio
            )
            if solicitud:
                return redirect(reverse("prestamo") + "?ok")
            else:
                return redirect(reverse("prestamo") + "?no")

    return render(request, "prestamo/prestamo.html", {"form": prestamo_form})
