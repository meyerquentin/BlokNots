from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))


class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))
    email = forms.CharField(label='Email', widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]