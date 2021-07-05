from django.contrib.auth.models import Group, User
from .models import *
def blog_menu(request):
    link_menu = Categorias.objects.all()
    return { 'link_menu': link_menu }

def list_prod(request):
    link_prod = Productos.objects.raw('SELECT * FROM frontend_productos ORDER BY fecha desc')[3:10]
    return { 'link_prod': link_prod }

def last_prod(request):
    lprod = Productos.objects.raw('SELECT * FROM frontend_productos ORDER BY fecha desc')[:3]
    return { 'lprod': lprod }

def grupo(request):
    users_in_group = Group.objects.get(name="Clientes").user_set.all()
    return { 'users_in_group': users_in_group }
