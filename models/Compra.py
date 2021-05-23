from database.Conection import Conection
from models.Model import Model

class Compra(Model):

    def __init__(self):
        self.__id = None
        self.__cantidad = None
        self.__precioTotal = None
        self.__producto_id = None
        self.__usuario_id = None
        self.__conection = Conection().get_conection()
    
    def get_all_for_usuario_id(self) -> list:
        sql = f'SELECT \
                    c.cantidad , \
                    c.precioTotal , \
                    c.producto_id \
                FROM \
                    compras c, \
                    productos p \
                where \
                    c.producto_id = p.id AND \
                    c.usuario_id = {self.__usuario_id} \
                ORDER BY c.id DESC'
        mycursor = self.__conection.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchall()
        compras = []
        for row in result:
            compra = Compra()
            compra.set_cantidad(row[0])
            compra.set_precioTotal(row[1])
            compra.set_producto_id(row[2])
            compras.append(compra)
        return [] if len(compras) == 0 else compras

    def get_all(self):
        mycursor = self.__conection.cursor()
        mycursor.execute('SELECT * FROM compras ORDER BY id DESC')
        result = mycursor.fetchall()
        compras = []
        for row in result:
            compra = Compra()
            compra.set_id(row[0])
            compra.set_cantidad(row[1])
            compra.set_precioTotal(row[2])
            compra.set_producto_id(row[3])
            compra.set_usuario_id(row[4])
            compras.append(compra)
        return [] if len(compras) == 0 else compras

    def save(self):
        query = "insert into compras(id, cantidad, precioTotal, producto_id, usuario_id) values (%s,%s,%s,%s,%s)"
        value = (None,self.get_cantidad(), self.get_precioTotal(), self.get_producto_id(), self.get_usuario_id())
        # Ejecuto la query
        self.__conection.cursor().execute(query, value)
        # Confirmo el insert
        self.__conection.commit()

    def update(self):
        pass

    def delete(self):
        sql = 'DELETE FROM compras WHERE id = %s '
        value = (self.get_id(), )
        # Ejecuto la query
        self.__conection.cursor().execute(sql, value)
        # Confirmo el delete
        self.__conection.commit()


    def reporte_de_ventas(self) -> dict:
        """ 
            return {
                'ventasRealizadas' : '...'
                'unidadesVendidas' : '...'
                'ingresos' : '...'
                'usuariosActivos' : '...'
            }
        """
        sql = ' \
            SELECT \
                COUNT(id) AS ventasRealizadas, \
                SUM(cantidad) AS unidadesVendidas, \
                SUM(precioTotal) AS ingresos, \
                COUNT( DISTINCT usuario_id) AS usuariosActivos \
            FROM \
                compras'
        mycursor = self.__conection.cursor()
        mycursor.execute(sql)
        result = mycursor.fetchone()
        return {
            'ventasRealizadas' : str(result[0]),
            'unidadesVendidas' : str(result[1]),
            'ingresos' : str(result[2]),
            'usuariosActivos' : str(result[3])
        }

    """ 
        GETTERS Y SETTERS
    """
    def get_id(self):
        return self.__id
    def get_cantidad(self):
        return self.__cantidad
    def get_precioTotal(self):
        return self.__precioTotal
    def get_producto_id(self):
        return self.__producto_id
    def get_usuario_id(self):
        return self.__usuario_id
    

    def set_id(self, id):
        self.__id = id
    def set_cantidad(self, cantidad):
        self.__cantidad = cantidad
    def set_precioTotal(self, precioTotal):
        self.__precioTotal = precioTotal
    def set_producto_id(self, producto_id):
        self.__producto_id = producto_id
    def set_usuario_id(self, usuario_id):
        self.__usuario_id = usuario_id
    