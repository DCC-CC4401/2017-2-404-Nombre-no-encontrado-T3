from django.contrib.auth.models import User


def getComunas():
    obj = User.objects.all().filter(profile__is_municipal=True)
    choices = []
    for user in obj:
        uname = user.username
        name = user.first_name
        choices.append((uname, name))
    return tuple(choices)


