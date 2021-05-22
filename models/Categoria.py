from database.Conection import Conection
from models.Model import Model

class Categoria(Model):
    
    def __init__(self):
        self.__id = ''
        self.__nombre = ''
        self.__conection = Conection().get_conection()

    def find(self, id):
        sql = f'SELECT \
                    * \
                FROM \
                    categorias \
                WHERE \
                    id = {id} '
        mycursor = self.__conection.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchone()
        if result == None:
            return None
        else:
            categoria = Categoria()
            categoria.set_id(result[0])
            categoria.set_nombre(result[1])
            return categoria

    def save(self):
        query = "insert into categorias(id, nombre) values (%s,%s)"
        value = (None,self.get_nombre())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self):
        sql = 'DELETE FROM categorias WHERE id = %s '
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
    