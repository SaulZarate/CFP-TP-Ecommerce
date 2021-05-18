
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

class AppController:

    def iniciar(self):
        categoria = Categoria()
        ciudad = Ciudad()
        compra = Compra()
        marca = Marca()
        pais = Pais()
        producto = Producto()
        provincia = Provincia()
        usuario = Usuario()
        
        print("Metodo iniciar de AppController")