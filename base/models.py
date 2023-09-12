from django.db import models
from django.contrib.auth.models import User

class Producto(models.Model):
    nombre = models.CharField(max_length=25)
    cantidad = models.IntegerField(blank=True, null=True)
    stock_minimo = models.IntegerField(blank=True, null=True)
    codigo_de_barras = models.IntegerField(blank=True, null=True)
    precio = models.IntegerField(blank=True, null=True)


    def __str__(self):
        return self.nombre