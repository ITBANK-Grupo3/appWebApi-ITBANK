from cProfile import label
from django import forms

CUENTAS=(
    ("CLASSIC","CLASSIC"),
    ("GOLD","GOLD"),
    ("BLACK","BLACK")
)

PRESTAMO_TIPO=(
    ("1","PERSONAL"),
    ("2","PRENDARIO"),
    ("3","HIPOTECARIO")
)

class loanForm(forms.Form):
    monto = forms.CharField(max_length=6, label="Ingrese el monto a solicitar")
    dni = forms.CharField(max_length=8, label="Ingrese su DNI")
    cuenta_seleccionada = forms.MultipleChoiceField(label="Seleccione una cuenta", choices=CUENTAS)
    tipo_prestamo = forms.MultipleChoiceField(label="seleccione el tipo de prestamo", choices=PRESTAMO_TIPO)
    fecha_inicio = forms.DateField(label="seleccione fecha de inicio del prestamo dd/mm/aa" )
