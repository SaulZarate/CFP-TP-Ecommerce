from models.Model import Model

class Ciudad(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__provincia_id = ''

    def find(self, id):
        pass

    def create(self):
        print('Metodo create de la clase Ciudad')

    def update(self):
        print('Metodo update de la clase Ciudad')

    def delete(self):
        print('Metodo delete de la clase Ciudad')

    """ 
        GETTERS Y SETTERS   
    """
    def get_id(self):
        return self.__id
    def get_nombre(self):
        return self.__nombre
    def get_provincia_id(self):
        return self.__provincia_id

    def set_id(self, id):
        self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_provincia_id(self, provincia_id):
        self.__provincia_id = provincia_id
    