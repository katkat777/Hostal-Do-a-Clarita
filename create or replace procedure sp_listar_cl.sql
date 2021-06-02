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
    v_fech_venc number,
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