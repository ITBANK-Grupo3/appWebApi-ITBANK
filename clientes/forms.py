from django import forms
from homebanking import settings


class RegistroForm(forms.Form):
    dni_cliente = forms.CharField(label="Dni", max_length=8, required=True)
    nombre = forms.CharField(label="Nombre", max_length=50, required=True)
    apellido = forms.CharField(
        label="Apellido",
        max_length=50,
        required=True,
    )
    email = forms.EmailField(label="Email", required=True)
    dob = forms.DateField(
        label="Fecha de nacimiento",
        input_formats=settings.DATE_INPUT_FORMATS,
        widget=forms.TextInput(attrs={"placeholder": "dd-mm-yyyy"}),
    )
    contraseña = forms.CharField(
        label="Contraseña", widget=forms.PasswordInput, max_length=50
    )
    rep_contraseña = forms.CharField(
        label="Repetir contraseña", widget=forms.PasswordInput, max_length=50
    )
