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


