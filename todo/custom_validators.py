from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def check_email(value):
    if User.objects.filter(email=value).exists():
        raise ValidationError('Account with that email already exists.')
    return value


class PasswordCheck:
    def validate(self, password, user=None):
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 character long')

    def get_help_text(self):
        return ''
