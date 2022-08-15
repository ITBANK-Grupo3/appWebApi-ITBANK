from django import forms
from homebanking import settings


PRESTAMO_TIPO = (("1", "PERSONAL"), ("2", "PRENDARIO"), ("3", "HIPOTECARIO"))


class PrestamoForm(forms.Form):
    monto = forms.IntegerField(label="Ingrese el monto a solicitar")
    tipo_prestamo = forms.CharField(
        label="Seleccione el tipo de prestamo",
        widget=forms.Select(choices=PRESTAMO_TIPO),
    )
    fecha_inicio = forms.DateField(
        label="Seleccione fecha de inicio del prestamo",
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.TextInput(attrs={"placeholder": "dd-mm-yyyy"}),
    )
