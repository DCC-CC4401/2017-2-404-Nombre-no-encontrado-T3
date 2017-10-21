from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Denuncia(models.Model):

    ESTADO = (
        (1, "Reportada"),
        (2, "Consolidada"),
        (3, "Verificada"),
        (4, "Cerrada"),
        (5, "Desechada"),
    )

    MALTRATO = (
        (0, ""),
        (1, "Abanono en la calle"),
        (2, "Exposición a altas temperaturas"),
        (3, "Falta de agua"),
        (4, "Falta de comida"),
        (5, "Violencia"),
        (6, "Venta ambulante"),
    )

    TIPOS = (
        (1, "Perro"),
        (2, "Gato"),
    )

    SEXO = (
        (1, "Macho"),
        (2, "Hembra"),
    )

    estado = models.CharField(max_length=15)
    calle = models.CharField(max_length=50)
    comuna = models.CharField(max_length=20)
    herido = models.CharField(max_length=2)
    color = models.CharField(max_length=10)
    sexo = models.IntegerField(choices=SEXO)
    tipo = models.IntegerField(choices=TIPOS)
    maltrato = models.IntegerField(choices=MALTRATO)
    comentario = models.CharField(max_length=40, blank=True)


class Animal(models.Model):

    TIPOS = (
        ("Perro", "Perro"),
        ("Gato", "Gato"),
    )

    SEXO = (
        (1, "Macho"),
        (2, "Hembra"),
    )

    EDAD = (
        (0, "< 1 año"),
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, "> 7 años"),
    )

    nombre = models.CharField(max_length=20)
    tipo = models.CharField(choices=TIPOS, max_length=10)
    foto = models.FileField(upload_to='media', default="img/profile", blank=True)
    sexo = models.IntegerField(choices=SEXO)
    edad = models.IntegerField(choices=EDAD)
    tiempo = models.CharField(max_length=10)


    def __str__(self):
        return '%s %s' % (self.nombre, self.tipo)


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
