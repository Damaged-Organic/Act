# act_project/act/metadata/utils.py
from django.apps import apps
from django.utils.html import strip_tags

from .settings import settings


def is_supported_model(url_name):
    return url_name in settings.SUPPORTED_MODELS


def get_supported_model_instance(url_name, id):
    if not is_supported_model(url_name):
        raise KeyError('Model by given `url_name` is not supported')

    model_tuple = settings.SUPPORTED_MODELS[url_name]
    model = apps.get_model(model_tuple[0], model_tuple[1])

    try:
        instance = model.objects.get(id=id)
    except model.DoesNotExist as e:
        raise model.DoesNotExist('Object by given `id` does not exist') from e

    return instance


def truncate_text(text, length):
    text = strip_tags(text)

    if len(text) > length:
        text = "{}...".format(text[:length].rsplit(' ', 1)[0].rstrip('.'))

    return text
