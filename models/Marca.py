from database.Conection import Conection
from models.Model import Model

class Marca(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        pass

    def save(self):
        query = "insert into marcas(id, nombre) values (%s,%s)"
        value = (None,self.get_nombre())
        
        # Obtengo el cursor
        cursor = self.__conection.cursor()
        # Ejecuto la query
        cursor.execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        print('Metodo update de la clase Marca')

    def delete(self):
        print('Metodo delete de la clase Marca')

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
    