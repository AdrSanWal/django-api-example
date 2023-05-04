from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authEndpoints.serializers import CustomUserSerializer, LoginSerializer
from core.models import CustomUser
from endpoints.views import CategoryViewSet, PersonViewSet, FilmViewSet


class AuthCategoryViewSet(CategoryViewSet):
    permission_classes = [IsAuthenticated]


class AuthPersonViewSet(PersonViewSet):
    permission_classes = [IsAuthenticated]


class AuthFilmViewSet(FilmViewSet):
    permission_classes = [IsAuthenticated]


class SignInView(APIView):
    serializer_class = CustomUserSerializer
    permission_classes = ()

    def post(self, request):
        """Crea un nuevo usuario"""

        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            username = serializer.validated_data.get('username')
            # the password2 field is deleted to allow us to create the user
            request.data.pop('password2')
            serializer.create(request.data)
            message = f'Usuario {username} creado'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.get_or_none(email=request.data.get('email'))
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            "email": user.email,
            "token": token.key
        })
