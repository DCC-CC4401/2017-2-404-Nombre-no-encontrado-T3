from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_user = models.BooleanField(default=True)
    is_municipal = models.BooleanField(default=False)
    is_ong = models.BooleanField(default=False)
    photo = models.ImageField(upload_to="img/userprofile")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Denuncia(models.Model):
    ESTADO = (
        ("RE", "Reportada"),
        ("CO", "Consolidada"),
        ("VE", "Verificada"),
        ("CE", "Cerrada"),
        ("DE", "Desechada"),
    )

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

    estado = models.CharField(choices=ESTADO, max_length=15, default="RE")
    calle = models.CharField(max_length=50)
    comuna = models.ForeignKey(User, on_delete=models.CASCADE)
    herido = models.CharField(choices=HERIDO, max_length=15)
    color = models.CharField(max_length=10)
    sexo = models.CharField(choices=SEXO, max_length=15)
    tipo = models.CharField(choices=TIPOS, max_length=10)
    maltrato = models.CharField(choices=MALTRATO, max_length=50)
    comentario = models.CharField(max_length=40, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.id, self.calle, self.estado)


class Animal(models.Model):
    TIPOS = (
        ("Perro", "Perro"),
        ("Gato", "Gato"),
    )

    SEXO = (
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
        ("D", "Desconocido"),
    )

    EDAD = (
        ("< 1 año", "< 1 año"),
        ("1", 1),
        ("2", 2),
        ("3", 3),
        ("4", 4),
        ("5", 5),
        ("6", 6),
        ("7", 7),
        ("> 7 años", "> 7 años"),
    )

    nombre = models.CharField(max_length=20)
    tipo = models.CharField(choices=TIPOS, max_length=10)
    foto = models.FileField(upload_to='img/', default="img/profile.png", blank=True)
    sexo = models.CharField(choices=SEXO, max_length=10)
    edad = models.CharField(choices=EDAD, max_length=15)
    tiempo = models.CharField(max_length=10)

    def __str__(self):
        return '%s %s' % (self.nombre, self.tipo)
