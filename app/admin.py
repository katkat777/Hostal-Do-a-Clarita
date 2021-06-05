from django.contrib import admin
from .models import Administrador, Cliente, ConsultaOrdenPedido, Descarga, Empleado, EstadoHabitacion, Factura,Habitacion, Huesped, Impresion,MetodoPago, OrdenCompra, OrdenPedido, Producto, Proveedor, RecepcionProducto, Registro, RegistroComedor, RelacionClienteReserva, RelacionProductoOrdenpedido, Reserva, SolicitudDeServicio, Transaccion, Usuario
# Register your models here.

admin.site.register(Administrador)
admin.site.register(Cliente)
admin.site.register(ConsultaOrdenPedido)
admin.site.register(Descarga)
admin.site.register(Empleado)
admin.site.register(EstadoHabitacion)
admin.site.register(Factura)
admin.site.register(Habitacion)
admin.site.register(Huesped)
admin.site.register(Impresion)
admin.site.register(MetodoPago)
admin.site.register(OrdenCompra)
admin.site.register(OrdenPedido)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(RecepcionProducto)
admin.site.register(RegistroComedor)
admin.site.register(Registro)
admin.site.register(RelacionProductoOrdenpedido)
admin.site.register(RelacionClienteReserva)
admin.site.register(Reserva)
admin.site.register(SolicitudDeServicio)
admin.site.register(Transaccion)
admin.site.register(Usuario)

