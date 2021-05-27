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