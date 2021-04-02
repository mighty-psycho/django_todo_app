from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Todo
from .custom_validators import check_email


class SignUpForm(UserCreationForm):
    email = forms.EmailField(validators=[check_email])

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo']


