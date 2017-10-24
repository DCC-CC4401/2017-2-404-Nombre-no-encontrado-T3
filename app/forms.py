from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from app.functions import getComunas
from .models import Denuncia


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
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class SignUpFormMunicipalUser(UserCreationForm):
    first_name = forms.CharField(
        label="Nombre de la Municipalidad",
        max_length=30,
        required=True,
        help_text='Requerido')
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
        help_text="Ingrese la misma contraseña para validar.",
    )

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class DenunciaForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DenunciaForm, self).__init__(*args, **kwargs)
        self.fields['comuna'] = forms.ChoiceField(
            choices=getComunas())

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
    comentario = forms.CharField(max_length=40, required=False)
    estado = forms.ChoiceField(choices=(("RE", "Reportada"),))

    def clean_comuna(self):
        comuna_name = self.cleaned_data['comuna']
        comuna = User.objects.all().get(username=comuna_name)
        print("cleaned")
        return comuna
    class Meta:
        model = Denuncia
        fields = ('tipo', 'sexo', 'color', 'herido', 'maltrato', 'calle', 'comuna', 'comentario', 'estado')


class ModifyDenunciaForm(forms.ModelForm):
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
    ESTADO = (
        ("RE", "Reportada"),
        ("CO", "Consolidada"),
        ("VE", "Verificada"),
        ("CE", "Cerrada"),
        ("DE", "Desechada"),
    )
    tipo = forms.ChoiceField(choices=TIPOS)
    sexo = forms.ChoiceField(choices=SEXO)
    color = forms.CharField(max_length=10)
    herido = forms.ChoiceField(choices=HERIDO)
    maltrato = forms.ChoiceField(choices=MALTRATO)
    calle = forms.CharField(max_length=50)
    comuna = forms.ChoiceField(choices=getComunas())
    comentario = forms.CharField(max_length=40, required=False)
    estado = forms.ChoiceField(choices=ESTADO)

    def clean_comuna(self):
        comuna_name = self.cleaned_data['comuna']
        comuna = User.objects.all().get(username=comuna_name)
        return comuna
    class Meta:
        model = Denuncia
        fields = ('tipo', 'sexo', 'color', 'herido', 'maltrato', 'calle', 'comuna', 'comentario', 'estado')
