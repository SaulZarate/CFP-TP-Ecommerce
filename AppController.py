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
from views.Menu import Menu

class AppController:

    """ user = Usuario()
        user.set_email('saul@gmail.com')
        user.set_clave('1234')
        usuarioLogeado = user.iniciar_sesion()
        print(usuarioLogeado) """
    
    def __init__(self):
        self.__usuarioLogeado = None
        self.__menuConsola = Menu()

    def iniciar(self):
        #self.__menuConsola.mostrar_menu('menu principal',{'1':'a','2':'b','3':'c','4':'d'})
        # logearse

        # mostrar todos los productos

        # comprar producto por id

        # ver productos comprados
        self.__elegir_productos()

    def __elegir_productos(self):
        productos = Producto().get_all()
        productosList = []
        for producto in productos:
            productosList.append({ str(producto.get_precio()) : producto.get_nombre() })
        self.__menuConsola.mostrar_productos('Productos de la tienda', productosList)

    def __set_usuario(self, usuario):
        self.__usuarioLogeado = usuario