from models.Model import Model

class Provincia(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__pais_id = ''

    def find(self, id):
        pass

    def create(self):
        print('Metodo create de la clase Provincia')

    def update(self):
        print('Metodo update de la clase Provincia')

    def delete(self):
        print('Metodo delete de la clase Provincia')

    """ 
        GETTERS Y SETTERS   
    """
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_pais_id(self):
        return self.__pais_id

    def set_id(self, id):
        self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_pais_id(self, pais_id):
        self.__pais_id = pais_id
    