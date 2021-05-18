from database.Conection import Conection
from models.Model import Model

class Producto(Model):
    
    def __init__(self):
        self.__id = None
        self.__nombre = None
        self.__precio = None
        self.__descripcion = None
        self.__categoria_id = None
        self.__marca_id = None
        self.__conection = Conection().get_conection()

    def find(self, id):
        pass

    def get_all(self):
        pass

    def save(self):
        query = "insert into productos (id, nombre, precio, descripcion, categoria_id, marca_id) values (%s,%s,%s,%s,%s,%s)"
        value = (None, self.get_nombre(), self.get_precio(), self.get_descripcion(), self.get_categoria_id(), self.get_marca_id())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self):
        query = 'DELETE FROM productos WHERE id=%s'
        value = (self.get_id(), )
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el delete
        self.__conection.commit()


    """ 
        GETTERS Y SETTERS
    """
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_precio(self):
        return self.__precio
    def get_descripcion(self):
        return self.__descripcion
    def get_categoria_id(self):
        return self.__categoria_id
    def get_marca_id(self):
        return self.__marca_id
        
    def set_id(self, id):
        self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_precio(self, precio):
        self.__precio = precio
    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
    def set_categoria_id(self, categoria_id):
        self.__categoria_id = categoria_id
    def set_marca_id(self, marca_id):
        self.__marca_id = marca_id