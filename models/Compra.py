from models.Model import Model

class Compra(Model):

    def __init__(self):
        self.__id = ''
        self.__precioTotal = ''
    
    def getAllForUsuarioId(self, usuario_id):
        pass

    def get_all(self):
        pass

    def create(self):
        print('Metodo create de la clase Compra')

    def update(self):
        print('Metodo update de la clase Compra')

    def delete(self):
        print('Metodo delete de la clase Compra')
    
    """ 
        GETTERS Y SETTERS
    """
    def get_id(self):
        return self.__id
    def get_precioTotal(self):
        return self.__precioTotal
        
    def set_id(self, id):
        self.__id = id
    def set_precioTotal(self, precioTotal):
        self.__precioTotal = precioTotal