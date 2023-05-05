from re import search

from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class UppercaseValidator(object):
    """The password must contain at least 1 uppercase letter."""

    def validate(self, password, user=None):

        if not search('[A-Z]', password):
            raise ValidationError(_("La contraseña debe contener al menos una mayúscula"))

    def get_help_text(self):
        return _(
            "La contraseña debe contener al menos una mayúscula"
        )
