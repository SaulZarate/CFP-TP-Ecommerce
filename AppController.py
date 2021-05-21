# Models
from models.Categoria import Categoria
from models.Ciudad import Ciudad
from models.Compra import Compra
from models.Marca import Marca
from models.Pais import Pais
from models.Producto import Producto
from models.Provincia import Provincia
from models.Usuario import Usuario

# Views
from views.Consola import Consola

class AppController:
    
    def __init__(self):
        self.__usuarioLogeado = None
        self.__viewConsola = Consola()

    def iniciar(self):
        datosRegistroUsuario = self.__registrarse()
        print(datosRegistroUsuario)
        #self.__menu_principal()
        #self.__productos_de_la_tienda()
        
        
    def __menu_principal(self)->int:
        return self.__viewConsola.mostrar_menu('Menu Principal',
        {'1':'Iniciar sesion',
        '2':'Registrarse',
        '':'',
        '0':'salir'}
        )
    
    def __registrarse(self)->dict:
        #self.__ciudad_id = ''
        datoSinCiudad = self.__viewConsola.inputs_formulario([
            {'text': 'Ingrese su DNI', 'type': 'str', 'name':'dni'},
            {'text': 'Ingrese su telefono', 'type': 'int', 'name':'tel'},
            {'text': 'Ingrese su nombre', 'type': 'str', 'name':'nombre'},
            {'text': 'Ingrese su email', 'type': 'str', 'name':'email'},
            {'text': 'Ingrese su contraseña', 'type': 'str', 'name':'clave'},
        ])
        print(datoSinCiudad)
        ciudadElegida = self.__viewConsola.select_formulario()
        

    def __iniciar_sesion(self)->int:
        pass

    def __menu_de_la_tienda(self)->int:
        return self.__viewConsola.mostrar_menu('Menu de la Tienda',
        {'1':'Ver los Productos de la tienda',
        '2':'Ver mis compras',
        '3':'Cerrar Sesion',
        '0':'salir'}
        )

    def __productos_de_la_tienda(self)->int:
        productos = Producto().get_all()
        productosList = []
        for producto in productos:
            productosList.append({ 
                'id': producto.get_id(),
                'nombre' : producto.get_nombre(), 
                'precio': str(producto.get_precio())
                })
        return self.__viewConsola.mostrar_todos_los_productos(productosList)
        
    def __set_usuario(self, usuario):
        self.__usuarioLogeado = usuario