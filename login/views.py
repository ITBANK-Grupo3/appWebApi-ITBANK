from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from database import models as models_db
import homebanking
from . import forms

import random


# Create your views here.
def register(request):
    registro_form = forms.RegistroForm

    if request.method == "POST":
        registro_form = registro_form(data=request.POST)

        if registro_form.is_valid():
            dni = request.POST.get("dni_cliente", "")
            nombre = request.POST.get("nombre", "")
            apellido = request.POST.get("apellido", "")
            email = request.POST.get("email", "")
            pwd = request.POST.get("rep_contraseña", "")
            dob = request.POST.get("dob", "")
            user = User.objects.create_user(dni, email, pwd)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            models_db.Cliente.objects.using("homebanking").create(
                customer_name=nombre,
                customer_surname=apellido,
                customer_dni=dni,
                dob=dob,
                branch_id=random.randint(1, 100),
            )
            return redirect(reverse("login"))
    return render(request, "login/register.html", {"form": registro_form})
