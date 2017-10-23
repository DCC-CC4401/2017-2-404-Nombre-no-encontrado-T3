from django.contrib.auth.models import User


def getComunas():
    obj = User.objects.all().filter(profile__is_municipal=True)
    choices = []
    for user in obj:
        uname = user.username
        name = user.first_name
        print(uname)
        choices.append((uname, name))
    return tuple(choices)


def parseDenuncia(den):
    #ESTADO = {
    #    "RE": "Reportada",
    #    "CO": "Consolidada",
    #    "VE": "Verificada",
    #    "CE": "Cerrada",
    #    "DE": "Desechada",
    #}

    MALTRATO = {
        "AB": "Abandono en la calle",
        "EX": "Exposición a altas temperaturas",
        "FA": "Falta de agua",
        "FC": "Falta de comida",
        "VI": "Violencia",
        "VA": "Venta ambulante",
    }

    TIPOS = {
        "P": "Perro",
        "G": "Gato",
    }

   # SEXO = {
   #     "M": "Macho",
   #     "H": "Hembra",
   #     "D": "Desconocido",
   # }

    HERIDO = {
        "S": "Sí",
        "N": "No",
        "D": "Desconocido",
    }

    return (MALTRATO[den.maltrato],
            TIPOS[den.tipo],
            den.calle,
            HERIDO[den.herido])


def parseDenunciaSet(Denuncia_set):
    lst = []
    for den in Denuncia_set:
        print("tipo = "+den.tipo)
        print("maltrato = "+den.maltrato)
        lst.append(parseDenuncia(den))
    print(lst)
    return tuple(lst)
