from django.contrib.auth.models import Group
from django.urls import reverse
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import *
from .forms import RegistroForm

# Create your views here.
def index(request):
    return render (request, "index.html")

def aboutus(request):
    return render (request, "aboutus.html")

def register(request):
    return render(request, "register.html")
    
def productos(request, prod_id):
    productoss = Productos.objects.get(id = prod_id)
    return render (request, "productos.html", {'productoss':productoss})

def listcategorias(request):
    cat_id = request.GET.get("Search")
    prodcat = Productos.objects.filter(categoria = cat_id)
    cate = Categorias.objects.filter(id = cat_id)
    return render (request, "listcategorias.html", {'prodcat':prodcat, 'cate':cate})

def categorias(request):
    categoriass = Categorias.objects.all()
    return render(request, 'categorias.html', {'categoriass':categoriass})

def searchresult(request):
    if request.method == 'GET':
        dato = request.GET.get("Search")
        result = Productos.objects.filter(nombre__icontains = dato)
        return render (request, "searchresult.html", {'result':result})

def cart(request):
    return render (request, "cart.html")

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save() 
            group = Group.objects.get(name='Clientes')
            user.groups.add(group)         
            return HttpResponseRedirect(reverse('login'))
    else:
        form = RegistroForm()
    return render(request, 'registration/register.html', {
        'form': form
        })