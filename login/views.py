from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from . import forms


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
            user = User.objects.create_user(dni, email, pwd)
            user.first_name = nombre
            user.last_name = apellido
            user.save()
            return redirect(reverse("login"))
    return render(request, "login/register.html", {"form": registro_form})
