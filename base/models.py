from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=False, blank=False, default='desconocido')
    nombre = models.CharField(max_length=25)
    cantidad = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    codigo_de_barras = models.IntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.nombre