
from models.Model import Model

class Usuario(Model):
    
    def __init__(self):
        self.__id = ''
        self.__dni = ''
        self.__nombre = ''
        self.__email = ''
        self.__clave = ''
        self.__isAdmin = ''
        self.__ciudad_id = ''

    def find(id):
        pass

    def create(self):
        print('Metodo create de Usuario')

    def update(self):
        print('Metodo update de Usuario')

    def delete(self):
        print('Metodo delete de Usuario')

    """ 
        GETTERS Y SETTERS
    """
    def get_id(self):
        return self.__id
    def set_id(self, id):
        self.__id = id
    
    def get_dni(self):
        return self.__dni
    def set_dni(self, dni):
        self.__dni = dni
    
    def get_nombre(self):
        return self.__nombre
    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email
    
    def get_clave(self):
        return self.__clave
    def set_clave(self, clave):
        self.__clave = clave
    
    def get_isAdmin(self):
        return self.__isAdmin
    def set_isAdmin(self, isAdmin):
        self.__isAdmin = isAdmin
    
    def get_ciudad_id(self):
        return self.__ciudad_id
    def set_ciudad_id(self, ciudad_id):
        self.__ciudad_id = ciudad_id