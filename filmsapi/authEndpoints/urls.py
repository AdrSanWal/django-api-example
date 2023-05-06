from django.urls import include, path
from rest_framework.routers import DefaultRouter

from authEndpoints import views


app_name = 'authEndpoints'

router = DefaultRouter()
router.register('categories', views.AuthCategoryViewSet)
router.register('people', views.AuthPersonViewSet)
router.register('films', views.AuthFilmViewSet)
router.register('users', views.AuthCustomUserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login', views.LoginView.as_view(), name='login'),
    path('auth/logout', views.LogOutView.as_view(), name='logout'),
    path('auth/signin', views.SignInView.as_view(), name='signin')
]
