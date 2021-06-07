# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Administrador(models.Model):
    rut = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='rut', primary_key=True)
    id_adm = models.CharField(unique=True, max_length=20)

    class Meta:
        managed = False
        db_table = 'administrador'


class AppCliente(models.Model):
    id = models.BigAutoField(primary_key=True)
    rut = models.CharField(unique=True, max_length=11, blank=True, null=True)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_cliente'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, blank=True, null=True)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, blank=True, null=True)
    first_name = models.CharField(max_length=150, blank=True, null=True)
    last_name = models.CharField(max_length=150, blank=True, null=True)
    email = models.CharField(max_length=254, blank=True, null=True)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cliente(models.Model):
    rut = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='rut', primary_key=True)
    id_cliente = models.CharField(unique=True, max_length=20)
    emp_cliente = models.CharField(max_length=20)
    id_huesped = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cliente'


class ConsultaOrdenPedido(models.Model):
    id_consulta_op = models.CharField(primary_key=True, max_length=20)
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')

    class Meta:
        managed = False
        db_table = 'consulta_orden_pedido'
        unique_together = (('id_consulta_op', 'proveedor_id_proveedor'),)


class Descarga(models.Model):
    id_descarga = models.CharField(primary_key=True, max_length=20)
    factura_id_factura = models.ForeignKey('Factura', models.DO_NOTHING, db_column='factura_id_factura')
    formato_descarga = models.CharField(max_length=20)
    fecha_descarga = models.DateField()

    class Meta:
        managed = False
        db_table = 'descarga'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200, blank=True, null=True)
    action_flag = models.IntegerField()
    change_message = models.TextField(blank=True, null=True)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, blank=True, null=True)
    model = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField(blank=True, null=True)
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Empleado(models.Model):
    rut = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='rut', primary_key=True)
    id_emp = models.CharField(unique=True, max_length=100)
    tipo_emp = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'empleado'


class EstadoHabitacion(models.Model):
    disponible = models.CharField(max_length=1)
    no_disponible_asignada = models.CharField(max_length=1)
    habitacion_id_habitacion = models.CharField(max_length=20)
    estado_habitacion_id = models.FloatField(primary_key=True)
    no_disponible_mantenimiento = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'estado_habitacion'


class Factura(models.Model):
    id_factura = models.CharField(primary_key=True, max_length=20)
    transaccion_id_transaccion = models.CharField(max_length=50)
    fecha_factura = models.CharField(max_length=50)
    detalle = models.CharField(max_length=50)
    total = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'factura'


class Habitacion(models.Model):
    id_habitacion = models.CharField(primary_key=True, max_length=20)
    precio = models.CharField(max_length=20)
    tipo_cama = models.CharField(max_length=20)
    caracteristicas = models.CharField(max_length=50)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva')
    accesorios = models.CharField(max_length=50)
    estado_habitacion_estado_habitacion_id = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'habitacion'


class Huesped(models.Model):
    rut = models.CharField(max_length=20, blank=True, null=True)
    id_huesped = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'huesped'


class Impresion(models.Model):
    id_impresion = models.CharField(primary_key=True, max_length=20)
    factura_id_factura = models.ForeignKey(Factura, models.DO_NOTHING, db_column='factura_id_factura')
    formato_impresion = models.CharField(max_length=20)
    fecha_impresion = models.DateField()

    class Meta:
        managed = False
        db_table = 'impresion'


class MetodoPago(models.Model):
    credito = models.CharField(max_length=50)
    debito = models.CharField(max_length=50)
    transaccion_id_transaccion = models.CharField(max_length=50)
    metodo_pago_id = models.FloatField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'metodo_pago'


class OrdenCompra(models.Model):
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp')
    id_orden_compra = models.CharField(primary_key=True, max_length=20)
    fecha_orden_compra = models.DateField()

    class Meta:
        managed = False
        db_table = 'orden_compra'
        unique_together = (('id_orden_compra', 'fecha_orden_compra'),)


class OrdenPedido(models.Model):
    id_pedido = models.CharField(primary_key=True, max_length=20)
    recepcion_producto_id_recepcion_producto = models.CharField(max_length=20)
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp')
    proveedor_id_proveedor = models.ForeignKey('Proveedor', models.DO_NOTHING, db_column='proveedor_id_proveedor')
    fecha_orden_pedido = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'orden_pedido'


class Producto(models.Model):
    id_producto = models.CharField(primary_key=True, max_length=20)
    precio = models.BigIntegerField()
    tipo_producto = models.CharField(max_length=20)
    stock = models.CharField(max_length=20)
    stock_critico = models.CharField(max_length=20)
    fech_venc = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'producto'


class Proveedor(models.Model):
    rut = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='rut', primary_key=True)
    id_proveedor = models.CharField(unique=True, max_length=20)
    emp_proveedor = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'proveedor'


class RecepcionProducto(models.Model):
    id_recepcion_producto = models.CharField(primary_key=True, max_length=20)
    orden_pedido_id_pedido = models.CharField(max_length=20)
<<<<<<< HEAD
    fecha_recepcion_pro = models.CharField(max_length=34)
=======
    fecha_recepcion_pro = models.CharField(max_length=20)
>>>>>>> a0abeabe48485c0aa95528dd16a264a951b6c9cf

    class Meta:
        managed = False
        db_table = 'recepcion_producto'


class Registro(models.Model):
    id_registro = models.CharField(primary_key=True, max_length=20)
    cuenta_id_cuenta = models.CharField(max_length=50)
    fecha_registro = models.DateField()
    administrador_id_adm = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='administrador_id_adm')

    class Meta:
        managed = False
        db_table = 'registro'


class RegistroComedor(models.Model):
    id_menu = models.CharField(primary_key=True, max_length=20)
    precio_menu = models.BigIntegerField()
    tipo_plato = models.CharField(max_length=20)
    tipo_servicio = models.CharField(max_length=20)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva')
    empleado_id_emp = models.ForeignKey(Empleado, models.DO_NOTHING, db_column='empleado_id_emp')

    class Meta:
        managed = False
        db_table = 'registro_comedor'


class RelacionClienteReserva(models.Model):
    cliente_rut = models.OneToOneField(Cliente, models.DO_NOTHING, db_column='cliente_rut', primary_key=True)
    reserva_id_reserva = models.ForeignKey('Reserva', models.DO_NOTHING, db_column='reserva_id_reserva')

    class Meta:
        managed = False
        db_table = 'relacion_cliente_reserva'
        unique_together = (('cliente_rut', 'reserva_id_reserva'),)


class RelacionProductoOrdenpedido(models.Model):
    orden_pedido_id_pedido = models.OneToOneField(OrdenPedido, models.DO_NOTHING, db_column='orden_pedido_id_pedido', primary_key=True)
    producto_id_producto = models.ForeignKey(Producto, models.DO_NOTHING, db_column='producto_id_producto')

    class Meta:
        managed = False
        db_table = 'relacion_producto_ordenpedido'
        unique_together = (('orden_pedido_id_pedido', 'producto_id_producto'),)


class Reserva(models.Model):
    id_reserva = models.CharField(primary_key=True, max_length=20)
    fecha_reserva = models.DateField()
    cliente_id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='cliente_id_cliente')
    transaccion_id_transaccion = models.ForeignKey('Transaccion', models.DO_NOTHING, db_column='transaccion_id_transaccion')

    class Meta:
        managed = False
        db_table = 'reserva'


class SolicitudDeServicio(models.Model):
    id_solicitud = models.CharField(primary_key=True, max_length=20)
    reserva_id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='reserva_id_reserva')
    transaccion_id_transaccion = models.ForeignKey('Transaccion', models.DO_NOTHING, db_column='transaccion_id_transaccion')

    class Meta:
        managed = False
        db_table = 'solicitud_de_servicio'


class Transaccion(models.Model):
    id_transaccion = models.CharField(primary_key=True, max_length=50)
    solicitud_de_servicio_id_solicitud = models.ForeignKey(SolicitudDeServicio, models.DO_NOTHING, db_column='solicitud_de_servicio_id_solicitud')
    factura_id_factura = models.CharField(max_length=20)
    metodo_pago_metodo_pago_id = models.FloatField()
    fecha_transaccion = models.DateField()
    reserva_id_reserva = models.ForeignKey(Reserva, models.DO_NOTHING, db_column='reserva_id_reserva')

    class Meta:
        managed = False
        db_table = 'transaccion'


class Usuario(models.Model):
    rut = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    fech_nac = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    registro_id_registro = models.ForeignKey(Registro, models.DO_NOTHING, db_column='registro_id_registro')
    correo_electronico = models.CharField(max_length=50)
    cuenta_id_cuenta = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'usuario'
