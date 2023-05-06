from datetime import timedelta

from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed

from config.settings import TOKEN_EXPIRATION_TIME


class CustomTokenAuthentication(TokenAuthentication):

    def expires_in(self, token):
        time_elapsed = timezone.now() - token.created
        token_time_remaining = timedelta(seconds=TOKEN_EXPIRATION_TIME) - time_elapsed
        return token_time_remaining

    def is_token_expired(self, token):
        return self.expires_in(token) < timedelta(seconds=0)

    def token_expired_handler(self, token):
        is_expired = self.is_token_expired(token)
        if is_expired:
            raise AuthenticationFailed(_('El token ha expirado.'))

    def authenticate_credentials(self, key):
        try:
            token = self.get_model().objects.select_related('user').get(key=key)
        except self.get_model().DoesNotExist:
            raise AuthenticationFailed(_('El token no es válido.'))

        if not token.user.is_active:
            raise AuthenticationFailed(_('El usuario está incativo o ha sido eliminado.'))

        self.token_expired_handler(token)

        return (token.user, token)
