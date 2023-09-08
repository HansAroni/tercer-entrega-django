from django.urls import path
from AppTerceraEntrega.views import * 

urlpatterns = [
    path('agrega-empleado/<nombre>/<apellido>/<email>/<celular>', empleado),
    path('lista_empleados/', lista_empleados),
    path('', inicio, name='inicio'),
    path('empleado/', empleado, name='empleado'),
    path('productos_nuevos/', productos_nuevos, name='productos_nuevos'),
    path('productos_usados/', productos_usados, name='productos_usados'),
    path('equipamiento/', equipamiento, name='equipamiento'),
    path('empleado_formulario/', empleado_formulario, name='empleado_formulario'),
    path('productosnuevos_formulario/', productosnuevos_formulario, name='productosnuevos_formulario'),
    path('productosusados_formulario/', productosusados_formulario, name='productosusados_formulario'),
    path('equipamientos_formulario/', equipamientos_formulario, name='equipamientos_formulario'),
    path('busqueda_apellido/', busqueda_apellido, name='busqueda_apellido'),
    path('buscar/', buscar, name='buscar')
]