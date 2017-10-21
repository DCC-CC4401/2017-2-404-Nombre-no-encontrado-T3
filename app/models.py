from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Denuncia(models.Model):
    MALTRATO = (
        (0, ""),
        (1, "abanono en la calle"),
        (2, "exposición a altas temperaturas"),
        (3, "falta de agua"),
        (4, "falta de comida"),
        (5, "violencia"),
        (6, "venta ambulante"),
    )

    TIPOS = (
        (1, "perro"),
        (2, "gato"),
    )

    SEXO = (
        (1, "macho"),
        (2, "hembra"),
    )

    estado = models.CharField(max_length=15)
    calle = models.CharField(max_length=50)
    comuna = models.CharField(max_length=20)
    herido = models.CharField(max_length=2)
    color = models.CharField(max_length=10)
    sexo = models.IntegerField(choices=SEXO)
    tipo = models.IntegerField(choices=TIPOS)
    maltrato = models.IntegerField(choices=MALTRATO, default=0)
    comentario = models.CharField(max_length=40)


class Animal(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=10)
    foto = models.ImageField(upload_to='media', default="img/profile", blank=True)
    sexo = models.CharField(max_length=10)
    edad = models.IntegerField()
    tiempo = models.CharField(max_length=10)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="img/userprofile")


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
