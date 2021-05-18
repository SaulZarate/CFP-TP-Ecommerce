CREATE TABLE categorias(
	id int(100) AUTO_INCREMENT NOT NULL,
    nombre varchar(100) not null,
    PRIMARY KEY(id)
);
CREATE TABLE marcas(
	id int(100) AUTO_INCREMENT NOT NULL,
    nombre varchar(100) not null,
    PRIMARY KEY(id)
);
CREATE TABLE productos(
	id int(100) AUTO_INCREMENT NOT NULL,
    nombre varchar(100) not null,
    precio double not null,
    categoria_id int(100) not null,
    marca_id int(100) not null,
    PRIMARY KEY(id),
	FOREIGN KEY (categoria_id) REFERENCES categorias(id),
    FOREIGN KEY (marca_id) REFERENCES marcas(id)
);


CREATE TABLE paises(
    id int(100) AUTO_INCREMENT NOT NULL,
    nombre varchar(100) not null,
    PRIMARY KEY(id)
);
CREATE TABLE provincias(
    id int(100) AUTO_INCREMENT NOT NULL,
    nombre varchar(100) not null,
    pais_id int(100) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(pais_id) REFERENCES paises(id)
);
CREATE TABLE ciudades(
    id int(100) AUTO_INCREMENT NOT NULL,
    nombre varchar(100) not null,
    provincia_id int(100) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(provincia_id) REFERENCES provincias(id)
);
CREATE TABLE usuarios(
    id int(100) AUTO_INCREMENT NOT NULL,
    dni varchar(100) not null,
    nombre varchar(100) not null,
    email varchar(100) not null,
    clave varchar(100) not null,
    isAdmin int(1) not null,
    ciudad_id int(100) not null,
    PRIMARY KEY(id),
    FOREIGN KEY(ciudad_id) REFERENCES ciudades(id)
);
CREATE TABLE compras(
    id int(100) AUTO_INCREMENT NOT NULL,
    cantidad int(100) not null,
    precioTotal double not null,
    producto_id int(100) not null,
    usuario_id int(100) not null,
    PRIMARY KEY(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
