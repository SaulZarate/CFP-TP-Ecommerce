from models.Model import Model

class Categoria(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''

    def find(self, id):
        pass

    def create(self):
        print('Metodo create de la clase Categoria')

    def update(self):
        print('Metodo update de la clase Categoria')

    def delete(self):
        print('Metodo delete de la clase Categoria')

    """ 
        GETTERS Y SETTERS
    """
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre

    def set_id(self, id):
        self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre
    