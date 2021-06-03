from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('contacto/', contacto, name="contacto"),
    path('galeria/', galeria, name="galeria"),
    path('registro/', registro, name="registro"),
    path('registrohabitacion/', registrohabitacion, name="registrohabitacion"),
    path('RegistroProducto/', RegistroProducto, name="RegistroProducto"),
    path('RegistroFactura/', RegistroFactura, name="RegistroFactura"),
    path('RegistroProveedor/', RegistroProveedor, name="RegistroProveedor"),
    path('RegistroMenu/', RegistroMenu, name="RegistroMenu"),
    path('reserva/', RegistroReserva, name="reserva"),
    path('RegistroEmpleado/', RegistroEmpleado, name="RegistroEmpleado"),
    path('RegistroRecepProducto/', RegistroRecepcionProducto, name="RegistroRecepProducto"),
    path('RegistroHuesped/', RegistroHuesped, name="RegistroHuesped"),



]
