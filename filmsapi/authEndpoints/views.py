from rest_framework import status
from rest_framework.authentication import get_authorization_header
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authEndpoints.serializers import CustomUserSerializer, LoginSerializer
from core.models import CustomUser
from endpoints.views import CategoryViewSet, PersonViewSet, FilmViewSet, CustomUserViewSet


class AuthCategoryViewSet(CategoryViewSet):
    permission_classes = [IsAuthenticated]


class AuthPersonViewSet(PersonViewSet):
    permission_classes = [IsAuthenticated]


class AuthFilmViewSet(FilmViewSet):
    permission_classes = [IsAuthenticated]


class AuthCustomUserViewSet(CustomUserViewSet):
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


class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

        # update token
        if not created:
            token.delete()
            token, created = Token.objects.get_or_create(user=user)

        return Response({
            "email": user.email,
            "token": token.key
        })


class LogOutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        print(get_authorization_header(request))
        _, token = request.headers['Authorization'].split(' ')
        token = Token.objects.filter(key=token).first()
        token.delete()
        return Response({'token_message': 'Token eliminado'},
                        status=status.HTTP_200_OK)
