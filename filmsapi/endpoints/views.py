from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter

from endpoints import serializers, pagination
from core.models import Category, Person, Film


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializers.CategorySerializer
    pagination_class = pagination.CustomPagination
    filter_backends = (OrderingFilter,)


class PersonViewSet(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = serializers.PersonSerializer
    pagination_class = pagination.CustomPagination
    filter_backends = (OrderingFilter,)

    def get_queryset(self):
        request = self.request.GET
        if 'q' in request:
            self.queryset = self.queryset.filter(name__icontains=request['q'])
        return self.queryset


class FilmViewSet(ModelViewSet):
    queryset = Film.objects.all()
    serializer_class = serializers.FilmSerializer
    pagination_class = pagination.CustomPagination
    filter_backends = (OrderingFilter,)

    def get_queryset(self):
        request = self.request.GET
        if 'q' in request:
            self.queryset = self.queryset.filter(title__icontains=request['q'])
        return self.queryset
