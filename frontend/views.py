from django.http.response import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from .models import *
from django.core import serializers

# Create your views here.
def index(request):
    return render (request, "index.html")

def aboutus(request):
    return render (request, "aboutus.html")

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

def register(request):
    return render (request, "registration/register.html")

def cart(request):
    return render (request, "cart.html")
