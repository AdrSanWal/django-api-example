from os import environ, path
from sys import path as syspath

from django import setup
from django.core.management import call_command


syspath.append(path.dirname(path.abspath(__file__)) + '/../..')

environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
setup()

from core.models import Category, Person, Film


class OperateDb():
    def delete_model_instances(self, model):
        instances = model.objects.all()
        instances.delete()
        print(f'delete all instances of {model.__name__} in db')

    def delete_all_instances(self):
        models = [Category, Person, Film]
        for model in models:
            self.delete_model_instances(model)
        print('delete all instances in db')

    def install_fixtures(self):
        call_command('loaddata', 'data.json')

    def drop_db(self):
        pass

b = OperateDb()

# b.delete_all_instances()
b.install_fixtures()
