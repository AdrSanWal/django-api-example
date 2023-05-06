from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from core.models import CustomUser


# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, attrs):
#         email = attrs.get('email')
#         password = attrs.get('password')

#         user = authenticate(request=self.context.get('request'),
#                             username=email, password=password)
#         if not user:
#             raise serializers.ValidationError(_('email o contraseña incorrectos'))

#         attrs['user'] = user
#         return attrs
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        user = authenticate(request=self.context.get('request'),
                            username=email, password=password)
        if not user:
            raise serializers.ValidationError(_('email o contraseña incorrectos'))

        attrs['user'] = user
        return attrs


class CustomUserSerializer(serializers.ModelSerializer):
    """Serializa un objeto de perfil de usuario"""
    password2 = serializers.CharField(label='Password',
                                      style={'input_type': 'password',
                                             'placeholder': 'Confirma la contraseña'})

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password': _("Las contraseñas no coinciden")})
        return attrs

    def create(self, validated_data):
        return CustomUser.objects.create_user(**validated_data)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'password2']
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password',
                          'placeholder': 'Contraseña'}
            },

        }
        read_only_fields = ('pk',)
