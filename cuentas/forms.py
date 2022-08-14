from django import forms
from homebanking import settings

lista = [("1", "Classic"), ("2", "Gold"), ("3", "Black")]


class SelectorForm(forms.Form):
    tipo_cliente = forms.CharField(
        label="Tipo a solicitar",
        max_length=8,
        required=True,
        widget=forms.Select(choices=lista),
    )
