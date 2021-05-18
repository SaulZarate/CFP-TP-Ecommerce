from database.Conection import Conection
from models.Model import Model

class Pais(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        pass

    def create(self):
        print('Metodo create de la clase Pais')

    def update(self):
        print('Metodo update de la clase Pais')

    def delete(self):
        print('Metodo delete de la clase Pais')

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
    