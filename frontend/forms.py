from django.forms.widgets import Widget
from .models import Categorias, Productos
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

class UploadImageForm(forms.ModelForm):
    nombre= forms.CharField(
         label='Nombre', widget=forms.TextInput(attrs={'name': 'nombre', 'placeholder':'Nombre', 'class':'formu'}), max_length=150, required=True)
    descripcion= forms.CharField(
        label='Descrip', widget=forms.Textarea(attrs={'name': 'descripcion', 'placeholder':'Descripción', 'class':'formu'}), required=True)
    categoria= forms.ModelChoiceField(queryset=Categorias.objects.all(),  label='Categoría',empty_label='Categoría',widget=forms.Select(attrs={'class':'formu'}))
    precio= forms.DecimalField(
        label='Precio', widget = forms.NumberInput(attrs={'name': 'precio', 'placeholder':'Precio', 'class':'formu'}), decimal_places=2, max_digits=15, required=True)
    foto= forms.ImageField(label='Foto',required=False, error_messages = {'invalid':"Sólo se admiten imágenes"}, widget=forms.FileInput)
    banner= forms.ImageField(label='Banner',required=False, error_messages = {'invalid':"Sólo se admiten imágenes"}, widget=forms.FileInput)

    class Meta:
        model = Productos
        fields = ['foto', 'banner','nombre', 'descripcion', 'categoria','precio']