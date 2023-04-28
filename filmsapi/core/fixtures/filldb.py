from os import environ, path
from django import setup
from sys import path as syspath

syspath.append(path.dirname(path.abspath(__file__)) + '/../..')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
setup()

from core.models import Category, Person, Film


def delete_all_instances():
    for c in Category.objects.all():
        c.delete()

    for p in Person.objects.all():
        p.delete()

    for f in Film.objects.all():
        f.delete()
    print('deleted')

delete_all_instances()

# TODO: script que rellene las fixtures
