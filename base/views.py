from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView , UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Producto





class Logueo(LoginView):
    template_name = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('ProductosView')

class ProductosView(LoginRequiredMixin, ListView):
    model = Producto
    context_object_name = 'productos'

    def get_context_data(self, **kwarg):
        context = super().get_context_data(**kwarg)
        context['productos'] = context['productos'].filter(usuario=self.request.user)
        return context


class ProductosDetalle(LoginRequiredMixin, DetailView):
    model = Producto
    
class AgrProducto(LoginRequiredMixin, CreateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('ProductosView')

class ModProducto(LoginRequiredMixin, UpdateView):
    model = Producto
    fields = '__all__'
    success_url = reverse_lazy('ProductosView')

class EliminarProducto(LoginRequiredMixin, DeleteView):
    model = Producto
    success_url = reverse_lazy('ProductosView')
    