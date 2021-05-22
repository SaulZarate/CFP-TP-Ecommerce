from database.Conection import Conection
from models.Model import Model

class Marca(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        sql = f'SELECT \
                    * \
                FROM \
                    marcas \
                WHERE \
                    id = {id} '
        mycursor = self.__conection.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result == None:
            return None
        else:
            marca = Marca()
            marca.set_id(result[0])
            marca.set_nombre(result[1])
            return marca

    def save(self):
        query = "insert into marcas(id, nombre) values (%s,%s)"
        value = (None,self.get_nombre())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        print('Metodo update de la clase Marca')

    def delete(self):
        query = "DELETE FROM marcas WHERE id =(%s)"
        value = (self.get_id(), )
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
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
    