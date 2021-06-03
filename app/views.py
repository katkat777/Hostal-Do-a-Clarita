from app.models import *
from django.shortcuts import render
from django.db import connection
import cx_Oracle

# Create your views here.

def home(request):
    return render(request, 'app/home.html')

def contacto(request):
    return render(request, 'app/contacto.html')

def galeria(request):
    return render(request, 'app/galeria.html')




def registrohabitacion(request):
    data = {
        'habitaciones':listado_habitaciones(),
    }
    if request.method == 'POST':
        id_habitacion = request.POST.get('id_habitacion')
        precio = request.POST.get('precio')
        tipo_cama = request.POST.get('tipo_cama')
        caracteristicas = request.POST.get('caracteristicas')
        reserva_id_reserva = request.POST.get('reserva_id_reserva')
        accesorios = request.POST.get('accesorios')
        estado_habitacion_estado_habitacion_id = request.POST.get('estado_habitacion_estado_habitacion_id')
        salida = agregar_habitacion(id_habitacion, precio, tipo_cama, caracteristicas, reserva_id_reserva, accesorios, estado_habitacion_estado_habitacion_id)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['habitaciones'] = listado_habitaciones()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/registrohabitacion.html', data)

def listado_habitaciones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HABITACIONES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista
    
def agregar_habitacion(id_habitacion, precio, tipo_cama, caracteristicas, reserva_id_reserva, accesorios, estado_habitacion_estado_habitacion_id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_HABITACION',[id_habitacion, precio, tipo_cama, caracteristicas, reserva_id_reserva, accesorios, estado_habitacion_estado_habitacion_id, salida])
    return salida.getvalue()




def registro(request):
    data = {
        'clientes':listado_clientes(),
    }

    if request.method == 'POST':
        rut = request.POST.get('rut')
        id_cliente = request.POST.get('cliente')
        emp_cliente = request.POST.get('emp_cliente')
        id_huesped = request.POST.get('huesped')
        salida = agregar_cliente(rut, id_cliente, emp_cliente, id_huesped)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['clientes'] = listado_clientes()
        else:
            data['mensaje'] = 'no se pudo guardar'
    
    return render(request, 'app/registro.html', data)


def listado_clientes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_CLIENTES", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

def agregar_cliente(rut, id_cliente, emp_cliente, id_huesped):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_CLIENTE',[rut, id_cliente, emp_cliente, id_huesped, salida])
    return salida.getvalue()



def RegistroProducto(request):
    data = {
        'productos':listado_productos(),
    }
    if request.method == 'POST':
        id_producto = request.POST.get('id_producto')
        precio = request.POST.get('precio')
        tipo_producto = request.POST.get('tipo_producto')
        stock = request.POST.get('stock')
        stock_critico = request.POST.get('stock_critico')
        fech_venc = request.POST.get('fech_venc')
        descripcion = request.POST.get('descripcion')
        salida = agregar_producto(id_producto, precio, tipo_producto, stock, stock_critico, fech_venc, descripcion)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['productos'] = listado_productos()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroProducto.html', data)


def agregar_producto(id_producto, precio, tipo_producto, stock, stock_critico, fech_venc, descripcion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PRODUCTO',[id_producto, precio, tipo_producto, stock, stock_critico, fech_venc, descripcion, salida])
    return salida.getvalue()


def listado_productos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista



##CU PROVEEDOR

def RegistroProveedor(request):
    data = {
        'proveedores':listado_proveedores(),
    }
    if request.method == 'POST':
        rut = request.POST.get('rut')
        id_proveedor = request.POST.get('id_proveedor')
        emp_proveedor = request.POST.get('emp_proveedor')
        salida = agregar_proveedor(rut, id_proveedor, emp_proveedor)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['proveedores'] = listado_proveedores()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroProveedor.html', data)

def agregar_proveedor(rut, id_proveedor, emp_proveedor):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_PROVEEDOR',[rut, id_proveedor, emp_proveedor, salida])
    return salida.getvalue()
    

def listado_proveedores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDOR", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista



#cu factura

def RegistroFactura(request):
    data = {
        'facturas':listado_facturas(),
    }
    if request.method == 'POST':
        id_factura = request.POST.get('id_factura')
        Transaccion_id_transaccion = request.POST.get('transaccion_id_transaccion')
        fecha_factura = request.POST.get('fecha_factura')
        detalle = request.POST.get('detalle')
        total = request.POST.get('total')
        
        salida = agregar_factura(id_factura, Transaccion_id_transaccion, fecha_factura, detalle, total)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['facturas'] = listado_facturas()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroFactura.html', data)


    
def agregar_factura(id_factura, Transaccion_id_transaccion, fecha_factura, detalle, total):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_FACTURA',[id_factura, Transaccion_id_transaccion, fecha_factura, detalle, total, salida])
    return salida.getvalue()
    

def listado_facturas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_FACTURAS", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista



##cu menu


def RegistroMenu(request):
    data = {
        'menus':listado_menus(),
    }
    if request.method == 'POST':
        id_menu = request.POST.get('id_factura')
        precio_menu = request.POST.get('transaccion_id_transaccion')
        tipo_plato = request.POST.get('tipo_plato')
        tipo_servicio = request.POST.get('tipo_servicio')
        reserva_id_reserva = request.POST.get('reserva_id_reserva')
        empleado_id_emp = request.POST.get('empleado_id_emp')
        
        salida = agregar_menu(id_menu, precio_menu, tipo_plato, tipo_servicio, reserva_id_reserva, empleado_id_emp)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['menus'] = listado_menus()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroMenu.html', data)


    
def agregar_menu(id_menu, precio_menu, tipo_plato, tipo_servicio, reserva_id_reserva, empleado_id_emp):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_MENU',[id_menu, precio_menu, tipo_plato, tipo_servicio, reserva_id_reserva, empleado_id_emp, salida])
    return salida.getvalue()
    

def listado_menus():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_MENU", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

#Reserva

def RegistroReserva(request):
    data = {
        'reservas':listado_reservas(),
    }
    if request.method == 'POST':
        id_reserva = request.POST.get('id_reserva')
        fecha_reserva = request.POST.get('fecha_reserva')
        cliente_id_cliente = request.POST.get('cliente_id_cliente')
        transaccion_id_transaccion = request.POST.get('transaccion_id_transaccion')
        salida = agregar_reserva(id_reserva, fecha_reserva, cliente_id_cliente,transaccion_id_transaccion)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['reservas'] = listado_reservas()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/reserva.html', data)

def agregar_reserva(id_reserva, fecha_reserva, cliente_id_cliente, transaccion_id_transaccion):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RESERVA',[id_reserva, fecha_reserva, cliente_id_cliente, transaccion_id_transaccion, salida])
    return salida.getvalue()
    

def listado_reservas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RESERVA", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista




## empleado

def RegistroEmpleado(request):
    data = {
        'empleados':listado_empleados(),
    }
    if request.method == 'POST':
        rut = request.POST.get('rut')
        id_emp = request.POST.get('id_emp')
        tipo_emp = request.POST.get('tipo_emp')
        
        
        salida = agregar_empleado(rut, id_emp, tipo_emp)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['empleados'] = listado_empleados()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroEmpleado.html', data)


    
def agregar_empleado(rut, id_emp, tipo_emp):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_EMPLEADO',[rut, id_emp, tipo_emp, salida])
    return salida.getvalue()
    

def listado_empleados():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_EMPLEADO", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista





  ## Recepcion producto
def RegistroRecepcionProducto(request):
    data = {
        'empleados':listado_recepciones(),
    }
    if request.method == 'POST':
        id_recepcion_producto= request.POST.get('id_recepcion_producto')
        orden_pedido_id_pedido = request.POST.get('orden_pedido_id_pedido')
        fecha_recepcion_pro = request.POST.get('fecha_recepcion_pro')
        
        
        salida = agregar_recepcion(id_recepcion_producto, orden_pedido_id_pedido, fecha_recepcion_pro)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['recepciones'] = listado_empleados()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroRecepProducto.html', data)


    
def agregar_recepcion(id_recepcion_producto, orden_pedido_id_pedido, fecha_recepcion_pro):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_RECEPCION',[id_recepcion_producto, orden_pedido_id_pedido, fecha_recepcion_pro, salida])
    return salida.getvalue()
    

def listado_recepciones():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RECEPCION", [out_cur])

    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista  

    #CU huesped

    def RegistroHuesped(request):
    data = {
        'huespedes':listado_huespedes(),
    }
    if request.method == 'POST':
        rut = request.POST.get('rut')
        id_huesped = request.POST.get('id_huesped')
        salida = agregar_huesped(rut, id_huesped)
        if salida == 1:
            data['mensaje'] = 'agregado correctamente'
            data['huespedes'] = listado_huespedes()
        else:
            data['mensaje'] = 'no se pudo guardar'

    return render(request, 'app/RegistroHuesped.html', data)

def agregar_huesped(rut, id_huesped):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('SP_AGREGAR_HUESPED',[rut, id_huesped, salida])
    return salida.getvalue()
    

def listado_huespedes():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_HUESPED", [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)

    return lista

