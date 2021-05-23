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
-- Agregar columna a tabla Productos
ALTER TABLE `productos` ADD `descripcion` TEXT NOT NULL AFTER `precio`;

/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
/* ~~~~~~~~~~~~ INSERTS ~~~~~~~~~~~~ */
/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */
-- Paises
INSERT INTO paises (id, 'nombre') VALUES (54, 'Argentina'), (598, 'Uruguay'), (34, 'España'), (49, 'Alemania');
-- Provincias
INSERT INTO provincias (id, nombre, pais_id) VALUES(1,'CABA',54),(5,'Santa Fe',54),(8,'La Pampa',54),(96,'Cataluña',34),(75,'Colonia',598),(77,'Montevideo',598);
-- Ciudades
INSERT INTO ciudades (id, nombre, provincia_id) VALUES(1,'CABA',1),(2,'Rosario',5),(3,'Santa Rosa',8),(71,'Barcelona',96),(12,'Carmelo',75),(15,'Montevideo',77);