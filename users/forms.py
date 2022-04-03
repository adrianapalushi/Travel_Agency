from django.contrib.auth.forms import UserCreationForm as AuthUserForm
from django.contrib.auth.forms import UsernameField

from .models import User


class UserCreationForm(AuthUserForm):
    class Meta:
        model = User
        fields = ('username',)
        field_classes = {"username": UsernameField}
