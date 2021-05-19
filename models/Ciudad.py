from database.Conection import Conection
from models.Model import Model

class Ciudad(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__provincia_id = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        pass

    def save(self):
        query = "insert into ciudades(id, nombre, provincia_id) values (%s,%s,%s)"
        value = (None,self.get_nombre(), self.get_provincia_id())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self):
        sql = 'DELETE FROM ciudades WHERE id = %s '
        value = (self.get_id(), )
        # Ejecuto la query
        self.__conection.cursor().execute(sql, value)
        # Confirmo el delete
        self.__conection.commit()

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
    