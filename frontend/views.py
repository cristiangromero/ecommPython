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

def categorias(request):
    categoriass = Categorias.objects.all()
    return render(request, 'categorias.html', {'categoriass':categoriass})

def searchresult(request):
    if request.method == 'GET':
        dato = request.GET.get("Search")
        result = Productos.objects.filter(nombre__icontains = dato)
        return render (request, "searchresult.html", {'result':result})

def login(request):
    return render (request, "login.html")

def register(request):
    return render (request, "register.html")

def cart(request):
    return render (request, "cart.html")