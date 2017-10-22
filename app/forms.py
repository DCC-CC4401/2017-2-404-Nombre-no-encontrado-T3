from django import forms
from .models import Denuncia
from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="Nombre",
        max_length=30,
        required=False,
        help_text='Opcional')
    last_name = forms.CharField(
        label="Apellido",
        max_length=30,
        required=False,
        help_text='Opcional.')
    email = forms.EmailField(max_length=254, help_text='Obligatorio, ingresa una dirección de correo válida.')

    error_messages = {
        'password_mismatch': "Las dos contraseñas no son iguales.",
    }

    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput,
        help_text="La contraseña debe contener al menos 8 caracteres. Su contraseña no puede ser una contraseña comúnmente utilizada\n ni tampoco enteramente numérica. ",
    )
    password2 = forms.CharField(
        label="Confirmación Contraseña",
        widget=forms.PasswordInput,
        strip=False,
        help_text="Ingrese la misma contraseña para validar",
    )
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


class DenunciaForm(forms.Form):

    MALTRATO = (
        ("AB", "Abandono en la calle"),
        ("EX", "Exposición a altas temperaturas"),
        ("FA", "Falta de agua"),
        ("FC", "Falta de comida"),
        ("VI", "Violencia"),
        ("VA", "Venta ambulante"),
    )

    TIPOS = (
        ("P", "Perro"),
        ("G", "Gato"),
    )

    SEXO = (
        ("M", "Macho"),
        ("H", "Hembra"),
        ("D", "Desconocido"),
    )

    HERIDO = (
        ("S", "Sí"),
        ("N", "No"),
        ("D", "Desconocido"),
    )

    tipo = forms.ChoiceField(choices=TIPOS)
    sexo = forms.ChoiceField(choices=SEXO)
    color = forms.CharField(max_length=10)
    herido = forms.ChoiceField(choices=HERIDO)
    maltrato = forms.ChoiceField(choices=MALTRATO)
    calle = forms.CharField(max_length=50)
    comuna = forms.CharField(max_length=20)
    comentario = forms.CharField(max_length=40, required=False)
    estado = forms.ChoiceField(choices= (("RE", "Reportada"),))