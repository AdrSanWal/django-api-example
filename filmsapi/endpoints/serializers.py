from rest_framework import serializers, status
from rest_framework.response import Response

from core.models import Category, Person, Film


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ('pk',)


class PersonSerializer(serializers.ModelSerializer):

    def to_representation(self, instance):
        instance.gender = dict(Person.GENDER_CHOICES)[instance.gender]
        return super().to_representation(instance)

    class Meta:
        model = Person
        fields = '__all__'
        read_only_fields = ('pk',)


class FilmSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    director = PersonSerializer(many=True)

    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = ('pk',)
