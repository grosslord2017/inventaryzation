from .models import *


# place for services logic


def add_to_history(curent_user, action, obj, description=''):
    History.objects.create(
        user=curent_user,
        action=action,
        obj=obj,
        description=description
    )


def all_objects(model):
    models_list = model.objects.all()
    return models_list