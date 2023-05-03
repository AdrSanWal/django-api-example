from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from endpoints import serializers
from core.models import Category, Person, Film


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    filter_backends = (OrderingFilter,)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer
    filter_backends = (OrderingFilter,)


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer
    filter_backends = (OrderingFilter,)
