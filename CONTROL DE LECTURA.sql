CREATE TABLE Lectura(
	id Serial Primary Key,
	Usuario varchar(200),
	Libro varchar(200),
	Autor varchar(200),
	Fecha date not null,
	Paginas_leidas integer not null,
	Meta_Paginas integer not null,
	Recomendaciones Text
);

