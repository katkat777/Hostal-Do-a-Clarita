create or replace procedure sp_listar_clientes(clientes out SYS_REFCURSOR)
is
begin
    open clientes for select * from cliente;
end;

create or replace procedure sp_agregar_cliente(
    v_rut varchar2,
    v_cliente varchar2,
    v_emp_cliente varchar2,
    v_huesped varchar2,
    v_salida out number
) is

begin
    insert into cliente(rut, id_cliente, emp_cliente, id_huesped)
    values(v_rut, v_cliente, v_emp_cliente, v_huesped);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;

create or replace procedure sp_agregar_habitacion(
    v_id_habitacion varchar2,
    v_precio varchar2,
    v_tipo_cama varchar2,
    v_caracteristicas varchar2,
    v_reserva_id_reserva varchar2,
    v_accesorios varchar2,
    v_estado_habitacion_estado_habitacion_id number,
    v_salida out number
) is

begin
    insert into habitacion(id_habitacion, precio, tipo_cama, caracteristicas, reserva_id_reserva, accesorios, estado_habitacion_estado_habitacion_id)
    values(v_id_habitacion, v_precio, v_tipo_cama, v_caracteristicas, v_reserva_id_reserva, v_accesorios, v_estado_habitacion_estado_habitacion_id);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;

create or replace procedure sp_listar_habitaciones(habitaciones out SYS_REFCURSOR)
is
begin
    open habitaciones for select * from habitacion;
end;

CREATE OR REPLACE  PROCEDURE sp_agregar_producto(
    v_id_producto varchar2,
    v_precio number,
    v_tipo_producto varchar2,
    v_stock varchar2,
    v_stock_critico varchar2,
    v_fech_venc date,
    v_descripcion varchar2,
    v_salida out number
) is

begin
    insert into producto(id_producto, precio, tipo_producto, stock, stock_critico, fech_venc, descripcion)
    values(v_id_producto, v_precio, v_tipo_producto, v_stock, v_stock_critico, v_fech_venc, v_descripcion);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;

CREATE OR REPLACE PROCEDURE SP_LISTAR_PRODUCTOS (productos out SYS_REFCURSOR)
is
begin
    open productos for select * from producto;
end;




CREATE OR REPLACE  PROCEDURE sp_agregar_factura(
    v_id_factura varchar2,
    v_transaccion_id_transaccion varchar2,
    v_fecha_factura date,
    v_detalle varchar2,
    v_total varchar2,
    v_salida out number
) is

begin
    insert into factura(id_factura, transaccion_id_transaccion,  fecha_factura,  detalle,  total)
    values(v_id_factura, v_transaccion_id_transaccion,  v_fecha_factura,  v_detalle,  v_total);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;


CREATE OR REPLACE PROCEDURE SP_LISTAR_FACTURAS (facturas out SYS_REFCURSOR)
is
begin
    open facturas for select * from factura;
end;






CREATE OR REPLACE  PROCEDURE sp_agregar_proveedor(
    v_rut varchar2,
    v_id_proveedor varchar2,
    v_emp_proveedor varchar2,
    v_salida out number
) is

begin
    insert into proveedor(rut, id_proveedor, emp_proveedor)
    values(v_rut, v_id_proveedor, v_emp_proveedor);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;


CREATE OR REPLACE PROCEDURE SP_LISTAR_PROVEEDOR (proveedores out SYS_REFCURSOR)
is
begin
    open proveedores for select * from proveedor;
end;





CREATE OR REPLACE  PROCEDURE sp_agregar_menu(
    v_id_menu varchar2,
    v_precio_menu number,
    v_tipo_plato varchar2,
    v_tipo_servicio varchar2,
    v_reserva_id_reserva varchar2,
    v_empleado_id_emp varchar2,
    v_salida out number
) is

begin
    insert into registro_comedor(id_menu, precio_menu, tipo_plato, tipo_servicio, reserva_id_reserva, empleado_id_emp)
    values(v_id_menu, v_precio_menu, v_tipo_plato, v_tipo_servicio, v_reserva_id_reserva, v_empleado_id_emp);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;


CREATE OR REPLACE PROCEDURE SP_LISTAR_MENU (menus out SYS_REFCURSOR)
is
begin
    open menus for select * from registro_comedor;
end;



CREATE OR REPLACE PROCEDURE sp_agregar_menu(
    v_id_reserva varchar2,
    v_fecha_reserva number,
    v_cliente_id_cliente varchar2,
    v_transaccion_id_transaccion varchar2,
    v_salida out number
) is





CREATE OR REPLACE  PROCEDURE sp_agregar_reserva(
    v_id_reserva varchar2,
    v_fecha_reserva number,
    v_cliente_id_cliente varchar2,
    v_transaccion_id_transaccion varchar2,
    v_salida out number
) is

begin
    insert into reserva(id_reserva, fecha_reserva, cliente_id_cliente, transaccion_id_transaccion)
    values( v_id_reserva, v_fecha_reserva, v_cliente_id_cliente, v_transaccion_id_transaccion);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;

CREATE OR REPLACE PROCEDURE SP_LISTAR_RESERVA (reservas out SYS_REFCURSOR)
is
begin
    open reservas for select * from reserva;
end;





CREATE OR REPLACE  PROCEDURE SP_REGISTRAR_EMPLEADO(
    v_rut varchar2,
    v_id_emp varchar2,
    v_tipo_emp varchar2,
    v_salida out number
) is

begin
    insert into empleado(rut, id_emp, tipo_emp)
    values(v_rut, v_id_emp, v_tipo_emp);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;


CREATE OR REPLACE PROCEDURE SP_LISTAR_EMPLEADO (empleados out SYS_REFCURSOR)
is
begin
    open empleados for select * from empleado;
end;





CREATE OR REPLACE  PROCEDURE SP_REGISTRAR_RECEPCION(
    v_id_recepcion_producto varchar2,
    v_orden_pedido_id_pedido varchar2,
    v_fecha_recepcion_pro date,
    v_salida out number
) is

begin
    insert into recepcion_producto(id_recepcion_producto, orden_pedido_id_pedido, fecha_recepcion_pro)
    values(v_id_recepcion_producto, v_orden_pedido_id_pedido, v_fecha_recepcion_pro);
    commit;
    v_salida:=1;

    exception
    when others then
        v_salida:=0;

end;


CREATE OR REPLACE PROCEDURE SP_LISTAR_RECEPCION (recepciones out SYS_REFCURSOR)
is
begin
    open recepciones for select * from recepcion_producto;
end;
