from models.Model import Model

class Producto(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__precio = ''
        self.__descripcion = ''
        self.__categoria_id = ''
        self.__marca_id = ''

    def find(self, id):
        pass

    def get_all(self):
        pass

    def create(self):
        print('Metodo create de la clase producto')

    def update(self):
        print('Metodo update de la clase producto')

    def delete(self):
        print('Metodo delete de la clase producto')

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