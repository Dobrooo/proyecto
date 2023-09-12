from django.urls import path
from .views import ProductosView, ProductosDetalle, AgrProducto, ModProducto, EliminarProducto, Logueo
from django.contrib.auth.views import LogoutView

urlpatterns = [path('', ProductosView.as_view(), name='ProductosView'),
               path('productos/<int:pk>', ProductosDetalle.as_view(), name='Productodetalle'),
                path('agregar-producto', AgrProducto.as_view(), name='AgrProducto'),
                path('modificar-producto/<int:pk>', ModProducto.as_view(), name='Modproducto'),
                path('eliminar-producto/<int:pk>', EliminarProducto.as_view(), name='ElimProducto'),
                path('login/', Logueo.as_view(), name = 'Logueo'),
                path('logout/', LogoutView.as_view(next_page='Logueo'), name = 'Logout')]
