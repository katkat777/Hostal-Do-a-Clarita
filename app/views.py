from app.models import AppCliente, Cliente
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
        'habitaciones':listado_habitaciones()
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
        'clientes':listado_clientes()
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
