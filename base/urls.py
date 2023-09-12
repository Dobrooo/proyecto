from django.urls import path
from .views import ProductosView, ProductosDetalle, AgrProducto

urlpatterns = [path('', ProductosView.as_view(), name='ProductosView'),
               path('productos/<int:pk>', ProductosDetalle.as_view(), name='Productodetalle'),
                path('agregar-producto', AgrProducto.as_view(), name='AgrProducto')]
