from database.Conection import Conection
from models.Model import Model

class Provincia(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__pais_id = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        pass

    def save(self):
        query = "insert into provincias(id, nombre, pais_id) values (%s,%s,%s)"
        value = (None,self.get_nombre(), self.get_pais_id())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self):
        sql = 'DELETE FROM provincias WHERE id = %s '
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
    def get_pais_id(self):
        return self.__pais_id

    def set_id(self, id):
        self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_pais_id(self, pais_id):
        self.__pais_id = pais_id
    