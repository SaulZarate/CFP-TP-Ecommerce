import base64

from database.Conection import Conection
from models.Model import Model

class Usuario(Model):
    
    def __init__(self):
        self.__id = 0
        self.__dni = ''
        self.__nombre = ''
        self.__email = ''
        self.__clave = ''
        self.__isAdmin = 0
        self.__ciudad_id = 0
        self.__conection = Conection().get_conection()

    def __str__(self) -> str:
        return f"Id({self.get_id()}) - Nombre: {self.get_nombre()} - DNI: {self.get_dni()} - Email: {self.get_email()} - Ciudad_id: {self.get_ciudad_id()}"

    def find(self, id):
        sql = "SELECT * FROM usuarios WHERE id = %s"
        value = (id, )
        cursor = self.__conection.cursor()
        cursor.execute(sql, value)
        userDB = cursor.fetchone()
        if userDB != None:
            usuario = Usuario()
            usuario.set_id(userDB[0])
            usuario.set_dni(userDB[1])
            usuario.set_nombre(userDB[2])
            usuario.set_email(userDB[3])
            usuario.set_isAdmin(userDB[5])
            usuario.set_ciudad_id(userDB[6])
        return None if userDB == None else usuario

    def get_all(self):
        mycursor = self.__conection.cursor()
        mycursor.execute('SELECT * FROM usuarios ORDER BY id ASC')
        result = mycursor.fetchall()
        usuarios = []
        for row in result:
            usuario = Usuario()
            usuario.set_id(row[0])
            usuario.set_dni(row[1])
            usuario.set_nombre(row[2])
            usuario.set_email(row[3])
            usuario.set_isAdmin(row[5])
            usuario.set_ciudad_id(row[6])
            usuarios.append(usuario)
        return usuarios

    def save(self):
        query = "insert into usuarios(id, dni, nombre, email, clave, isAdmin, ciudad_id) values (%s,%s,%s,%s,%s,%s,%s)"
        value = (None, self.get_dni(), self.get_nombre(), self.get_email(), self.encriptarPass(self.get_clave()), self.get_isAdmin(), self.get_ciudad_id())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self) -> bool:
        try:
            sql = 'DELETE FROM usuarios WHERE id = %s '
            value = (self.get_id(), )
            # Ejecuto la query
            self.__conection.cursor().execute(sql, value)
            # Confirmo el delete
            self.__conection.commit()
            return True
        except:
            return False

    # INICIO DE SESION
    def existe_dni(self) -> bool:
        dniUsuarios = list( map(lambda user: user.get_dni(), self.get_all()) )
        return self.__dni in dniUsuarios

    def existe_email(self) -> bool:
        emailUsuarios = list( map(lambda user: user.get_email(), self.get_all()) )
        return self.__email in emailUsuarios
        
    def iniciar_sesion(self) -> object:
        sql = "SELECT * FROM usuarios WHERE email = %s and clave = %s"
        value = (self.get_email(), self.encriptarPass(self.get_clave()))
        cursor = self.__conection.cursor()
        cursor.execute(sql, value)
        
        result = cursor.fetchone()
        return None if result == None else self.find(result[0])
    
    """ 
        ENCRIPTACIONES
    """
    def encriptarPass(self, password):
        return base64.encodebytes(bytes(password, 'utf-8')).decode('utf-8')
    def desencriptarPass(self,password):
        return base64.decodebytes(password.encode("UTF-8")).decode('utf-8')

    
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