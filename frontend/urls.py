from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('searchresult', views.searchresult, name='searchresult'),
    path('<int:prod_id>', views.productos, name='productos'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('cart', views.cart, name='cart'),
    path('categorias', views.categorias, name='categorias'),
    path('listcategorias', views.listcategorias, name='listcategorias'),
]