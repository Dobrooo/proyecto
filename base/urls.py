from django.urls import path
from .views import ProductosView, ProductosDetalle, AgrProducto, ModProducto, EliminarProducto

urlpatterns = [path('', ProductosView.as_view(), name='ProductosView'),
               path('productos/<int:pk>', ProductosDetalle.as_view(), name='Productodetalle'),
                path('agregar-producto', AgrProducto.as_view(), name='AgrProducto'),
                path('modificar-producto/<int:pk>', ModProducto.as_view(), name='Modproducto'),
                path('eliminar-producto/<int:pk>', EliminarProducto.as_view(), name='ElimProducto')]
