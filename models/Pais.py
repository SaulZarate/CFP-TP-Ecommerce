from database.Conection import Conection
from models.Model import Model

class Pais(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        pass

    def save(self):
        query = "insert into paises(id, nombre) values (%s,%s)"
        value = (None,self.get_nombre())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self):
        sql = 'DELETE FROM paises WHERE id = %s '
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

    def set_id(self, id):
        self.__id = id
    def set_nombre(self, nombre):
        self.__nombre = nombre
    