# Database
from database.Conection import Conection

# Models
from models.Categoria import Categoria
from models.Ciudad import Ciudad
from models.Compra import Compra
from models.Marca import Marca
from models.Pais import Pais
from models.Producto import Producto
from models.Provincia import Provincia
from models.Usuario import Usuario

# Views

""" 
    categoria = Categoria()
    ciudad = Ciudad()
    compra = Compra()
    marca = Marca()
    pais = Pais()
    producto = Producto()
    provincia = Provincia()
    usuario = Usuario() 
"""

class AppController:

    def __init__(self):
        self.__conection = Conection().get_conection()

    def iniciar(self):
        db = self.__conection.cursor()

        db.execute("SHOW TABLES")
        for database in db:
            print(database)