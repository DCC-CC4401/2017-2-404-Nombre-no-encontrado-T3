from django.contrib.auth.models import User


def getComunas():
    choices = []
    try:
        obj = User.objects.filter(profile__is_municipal=True)
        for user in obj:
            uname = user.username
            name = user.first_name
            choices.append((uname, name))
        return tuple(choices)
    except:
        pass
    return tuple(choices)

