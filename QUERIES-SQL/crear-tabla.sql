-- tabal vetnas_2020 ejercicio de queries sql
CREATE DATABASE practicar;
USE practicar;
CREATE TABLE IF NOT EXISTS VENTAS_2020 (
	Dia int not null,
	Mes int not null, 
	Anio int not null,
	Producto varchar (25) not null,
	id int PRIMARY KEY,
    cliente varchar (25) not null,
	valor int not null
);

INSERT INTO VENTAS_2020 (Dia, Mes, Anio, Producto, id, cliente, valor)
values  (1,2,1998,'Bocina',24, "jota", 528),
        (12,4,2004, 'Auriculares', 31, "jita", 240),
        (14,8,2016,'Auriculares', 14, "jajajja",  315),
        (16,10,2019,'Bocina',200, "daniela",1050),
        (21,12,2020,'Bocina',304, "andres", 680);