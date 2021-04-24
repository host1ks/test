from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.forms import ModelForm
from .models import Subscribe


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Имя пользователя'),
    password = forms.CharField(label='Пароль'),


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ["sub_user", "blog"]
