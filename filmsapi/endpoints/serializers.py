from rest_framework import serializers, status
from rest_framework.fields import empty
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

    def many_to_many_representation(self, instance, representation):
        many_to_many_fields = {
            "category": instance.category,
            "director": instance.director,
            "characters": instance.characters,
            "screenplay": instance.screenplay,
            "story": instance.story,
            "novel": instance.novel,
            "writer": instance.writer,
            "cast": instance.cast
        }
        for field in many_to_many_fields:
            if field == 'category':
                data = CategorySerializer(many_to_many_fields[field], many=True).data
            else:
                data = PersonSerializer(many_to_many_fields[field], many=True).data
            representation[field] = [{"id": d['id'], "name": d['name']} for d in data]

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        self.many_to_many_representation(instance, representation)
        # categories = CategorySerializer(instance.category, many=True).data
        # director = PersonSerializer(instance.director, many=True).data
        # representation['category'] = [{"id": d['id'], "name": d['name']} for d in categories]
        # representation['director'] = [{"id": d['id'], "name": d['name']} for d in director]
        return representation

    class Meta:
        model = Film
        fields = '__all__'
        read_only_fields = ('pk',)
