CREATE TABLE gastos(
	id serial primary key,
	usuario varchar(200),
	alimento varchar(200),
	cantidad decimal not null,
	costo decimal not null
);