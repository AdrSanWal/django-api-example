from rest_framework.serializers import Serializer

from core.models import Category, Person, Film


class CategorySerializer(Serializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('pk')


class PersonSerializer(Serializer):
    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ('pk')


class FilmSerializer(Serializer):
    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = ('pk')
