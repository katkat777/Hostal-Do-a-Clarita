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

def registro(request):
    data = {
        'clientes':listado_clientes()
    }

    #agregar_cliente(100,234,44,54)

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