from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class RegistroForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'name': 'Username', 'placeholder':'Usuario'}), max_length=150, required=True)
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'name': 'Password', 'placeholder':'Password'}), max_length=30, required=True)
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'name': 'Confirm Password', 'placeholder':'Confirmar Password'}), max_length=30, required=True)
    email = forms.EmailField(
        widget=forms.TextInput(attrs={'name': 'Email', 'placeholder': 'Email'}), max_length=254, required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', )