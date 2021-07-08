from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField
from django.contrib.auth.models import User

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=200)
    def __str__(self):
        return u'{0}'.format(self.nombre)

class Productos(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=11, decimal_places=2)
    descripcion = models.TextField()
    foto = models.ImageField(upload_to='fotos')
    banner = models.ImageField(upload_to='banners')
    fecha = models.DateTimeField(auto_now_add=True)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    class Meta:
        ordering = ['nombre']

class Carrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="usuario")
    producto =  models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    def __str__(self):
        return self.productos