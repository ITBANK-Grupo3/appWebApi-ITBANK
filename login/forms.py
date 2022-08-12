import email
from django import forms


class RegistroForm(forms.Form):
    dni_cliente = forms.CharField(
        widget=forms.TextInput({"placeholder": "DNI"}), max_length=8, required=True
    )
    nombre = forms.CharField(
        widget=forms.TextInput({"placeholder": "Nombre"}), max_length=50, required=True
    )
    apellido = forms.CharField(
        widget=forms.TextInput({"placeholder": "Apellido"}),
        max_length=50,
        required=True,
    )
    email = forms.EmailField(
        widget=forms.TextInput({"placeholder": "Email"}), required=True
    )
    contraseña = forms.CharField(widget=forms.PasswordInput, max_length=50)
    rep_contraseña = forms.CharField(widget=forms.PasswordInput, max_length=50)
