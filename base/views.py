from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Producto

class ProductosView(ListView):
    model = Producto



class ProductosDetalle(DetailView):
    model = Producto
    
class AgrProducto(CreateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('ProductosView')

class ModProducto(UpdateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('ProductosView')

class EliminarProducto(DeleteView):
    model = Producto
    success_url = reverse_lazy('ProductosView')
    