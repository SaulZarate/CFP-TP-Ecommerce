from database.Conection import Conection
from models.Model import Model

class Compra(Model):

    def __init__(self):
        self.__id = ''
        self.__cantidad = ''
        self.__precioTotal = ''
        self.__producto_id = ''
        self.__usuario_id = ''
        self.__conection = Conection().get_conection()
    
    def getAllForUsuarioId(self, usuario_id):
        pass

    def get_all(self):
        pass

    def save(self):
        print('Metodo create de la clase Compra')

    def update(self):
        print('Metodo update de la clase Compra')

    def delete(self):
        print('Metodo delete de la clase Compra')
    
    """ 
        GETTERS Y SETTERS
    """
    def get_id(self):
        return self.__id
    def get_cantidad(self):
        return self.__cantidad
    def get_precioTotal(self):
        return self.__precioTotal
    def get_producto_id(self):
        return self.__producto_id
    def get_usuario_id(self):
        return self.__usuario_id
    

    def set_id(self, id):
        self.__id = id
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    def set_precioTotal(self, precioTotal):
        self.__precioTotal = precioTotal
    def set_producto_id(self, producto_id):
        self.__producto_id = producto_id
    def set_usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id
    