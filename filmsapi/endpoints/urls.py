from django.urls import include, path
from rest_framework.routers import DefaultRouter

from endpoints.views import PersonViewSet, FilmViewSet, CategoryViewSet, CustomUserViewSet


app_name = 'endpoints'

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('people', PersonViewSet)
router.register('films', FilmViewSet)
router.register('users', CustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
