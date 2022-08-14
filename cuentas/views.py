from django.shortcuts import render
from . import forms

# Create your views here.
def paquetes(request):
    form = forms.SelectorForm
    return render(request, "cuentas/paquetes.html", {"form": form})
