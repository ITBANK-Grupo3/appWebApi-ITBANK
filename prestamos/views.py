from django.shortcuts import render,redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import loanForm
from render_templates.views import home
from database import models as db_models


# Create your views here.
@login_required(login_url="/home/")
def prestamo(request):
    # cliente = db_models.Cliente.objects.using('homebanking').all()
    # cuenta = db_models.Cuenta.objects.using('homebanking').all()
    prestamo_form = loanForm
    if not request.user.is_authenticated:
        home(request)
    if request.method == "POST":
        prestamo_form = prestamo_form(data=request.POST)
        if prestamo_form.is_valid():
            monto = request.POST.get('monto','')
            dni = request.POST.get('dni', '')
            cuenta_seleccionada = request.POST.get('cuenta_seleccionada','')
            tipo_prestamo = request.POST.get('tipo_prestamo','')
            fecha_inicio = request.POST.get('fecha_inicio','')
            
            cliente = db_models.Cliente.objects.using('homebanking').filter(customer_dni = int(dni))
            cuenta = db_models.Cuenta.objects.using('homebanking').filter(customer_id = cliente[0].customer_id)
            # for x in cuenta:
            #     if cuenta_seleccionada == "CLASSIC" and cuenta[0].tipo_cuenta == 1:
            #         c= db_models.Cuenta.objects.get(cutomer_id = cliente[0].customer_id)
            #         c.balance = int(request.POST.get('monto',''))
            #         c.save()
            #     elif cuenta_seleccionada == "GOLD" and cuenta[0].tipo_cuenta == 2:
            #         c= db_models.Cuenta.objects.get(cutomer_id = cliente[0].customer_id)
            #         c.balance = request.POST.get('monto','')
            #         c.save()
            #     elif cuenta_seleccionada == "BLACK" and cuenta[0].tipo_cuenta == 3:
            #         c= db_models.Cuenta.objects.get(cutomer_id = cliente[0].customer_id)
            #         c.balance = int(request.POST.get('monto',''))
            #         c.save()
            
            return redirect(reverse('prestamo')+"?ok" ) 
            
    return render(request, "prestamo/prestamo.html",{"form": prestamo_form})