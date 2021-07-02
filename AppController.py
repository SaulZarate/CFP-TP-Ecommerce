# Models
from time import time
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
        while True:
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~ MENU PRINCIPAL ~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            opcionMenuPrincipal = self.__menu_principal()

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~ INICIAR DE SESION ~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            if opcionMenuPrincipal == 1:

                # ---- INICIO DE SESION ----
                if self.__usuarioLogeado == None:
                    if self.__iniciar_sesion() == 0: # IR AL MENU PRINCIPAL
                        continue
                
                # ---- VISTAS DEL ADMIN ----
                if self.__usuarioLogeado.get_isAdmin():
                    opctionAdmin = self.__seccion_del_administrador()

                    if opctionAdmin == 0: # CERRAR APP
                        break
                    self.__usuarioLogeado = None
                    continue

                # ---- VISTAS DEL CLIENTE ----
                if self.__seccion_del_cliente() == 3: # CERRAR SESION
                    self.__usuarioLogeado = None
                else: # CERRAR APP
                    break

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~ REGISTRAR USUARIO ~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            elif opcionMenuPrincipal == 2: 
                self.__registrar_usuario()

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # ~~~~~~~~ CERRAR APP ~~~~~~~~
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            else: 
                break
        
        # CERRAR APP
    
    """ 
        INICIO DE SESION & REGISTRO 
    """
    def __registrar_usuario(self):
        datosUsuario = self.__pedir_datos_para_registrarse()
        usuario = Usuario()
        usuario.set_dni(str(datosUsuario['dni']))
        usuario.set_nombre(datosUsuario['nombre'])
        usuario.set_email(datosUsuario['email'])
        usuario.set_clave(datosUsuario['clave'])
        usuario.set_ciudad_id(datosUsuario['ciudad_id'])

        # Validar DNI unico
        while True:
            if usuario.existe_dni():
                inputDNI = self.__viewConsola.inputs_formulario([{
                    'text' : '* El dni ingresado ya existe, ingrese otro: \n  DNI',
                    'type' : 'int',
                    'name' : 'dni'
                }])
                usuario.set_dni(inputDNI['dni'])
            else:
                break
        
        # Validacion del email
        while True :
            if usuario.existe_email():
                inputEmail = self.__viewConsola.inputs_formulario([{
                    'text' : '* El email ingresado ya existe, ingrese otro: \n  Email',
                    'type' : 'email',
                    'name' : 'email'
                }])
                usuario.set_email(inputEmail['email'])
            else:
                break

        # Registrar al usuario
        usuario.save()
        # Muestro mensaje
        self.__viewConsola.mostrar_mensaje('* Usuario registrado correctamente')
        self.__viewConsola.limpiar_consola(2)

    def __pedir_datos_para_registrarse(self) -> dict:
        # Inputs
        inputsUsuario = self.__viewConsola.inputs_formulario([
            {'text': 'Ingrese su DNI sin puntos', 'type': 'int', 'name':'dni'},
            {'text': 'Ingrese su nombre', 'type': 'str', 'name':'nombre'},
            {'text': 'Ingrese su email', 'type': 'email', 'name':'email'},
            {'text': 'Ingrese su contraseña', 'type': 'str', 'name':'clave'},
        ])
        # Ciudad
        ciudadesValidas = []
        for ciudad in Ciudad().getAll():
            ciudadesValidas.append({
                'id': ciudad.get_id(),
                'value': ciudad.get_nombre()
            })
        ciudadElegida = self.__viewConsola.select_formulario({
            'values': ciudadesValidas,
            'text': 'Ingrese el codigo de su ciudad',
            'name': 'ciudad_id',
            'title' : 'CIUDADES'
        })
        inputsUsuario.update(ciudadElegida)
        return inputsUsuario

    def __iniciar_sesion(self) -> Usuario:
        usuario = Usuario()
        while True:
            self.__viewConsola.limpiar_consola()
            self.__viewConsola.mostrar_mensaje('***************************')
            self.__viewConsola.mostrar_mensaje('**** INICIAR DE SESION ****')
            self.__viewConsola.mostrar_mensaje('***************************\n')
            inputsUsuario = self.__viewConsola.inputs_formulario([
                { 'text' : 'Ingrese su email', 'type' : 'email', 'name' : 'email' },
                { 'text' : 'Ingrese su contraseña', 'type' : 'str', 'name' : 'clave' }
            ])
            usuario.set_email(inputsUsuario['email'])
            usuario.set_clave(inputsUsuario['clave'])
            
            result = usuario.iniciar_sesion()
            if not usuario.existe_email() :
                mensaje = '* El email ingresado no esta registrado'
            elif result == None:
                mensaje = '* Contraseña incorrecta'
            else:
                self.__viewConsola.limpiar_consola()
                self.__usuarioLogeado = result
                return result

            self.__viewConsola.mostrar_mensaje(mensaje)
            salir =  input('* Desea volver a intentarlo ? si/no: ')
            if salir == 'no': 
                self.__viewConsola.limpiar_consola()
                return 0

    """ 
        SECCION DEL ADMINISTRADOR & CLIENTE
    """
    def __seccion_del_administrador(self) -> int:
        """ 
            0 = Cerrar App | 3 = Cerrar sesion
        """
        while True: 
            menuPrincipalDelAdmin = self.__admin_menu_principal()

            # ~~~~~~~~ PRODUCTOS ~~~~~~~~
            if menuPrincipalDelAdmin == 1:
                # Id del producto
                productoId = self.__admin_productos_de_la_tienda()

                # 0 = volver al menuPrincipalDelAdmin
                if productoId != 0: 
                    # Edita el producto
                    self.__edit_producto_de_la_tienda(productoId)
            
            # ~~~~~~~~ VENTAS ~~~~~~~~
            elif menuPrincipalDelAdmin == 2:
                self.__admin_registro_de_ventas()
            
            # ~~~~~~~~ CATEGORIAS ~~~~~~~~
            elif menuPrincipalDelAdmin == 3:
                self.__admin_mostrar_categorias()
            
            # ~~~~~~~~ MARCAS ~~~~~~~~
            elif menuPrincipalDelAdmin == 4:
                self.__admin_mostrar_marcas()
            
            # ~~~~~~~~ USUARIOS ~~~~~~~~
            elif menuPrincipalDelAdmin == 5:
                usuarioId = self.__admin_mostrar_usuarios()

                if usuarioId != 0:
                    self.__admin_eliminar_usuario(usuarioId)
            
            # ~~~~~~~~ CERRAR SESION ~~~~~~~~ 
            elif menuPrincipalDelAdmin == 9:
                return 3
            
            # ~~~~~~~~ SALIR ~~~~~~~~
            else:
                return 0

    def __seccion_del_cliente(self) -> int:
        """ 
            0 = Cerrar App | 3 = Cerrar sesion
        """
        while True:
            opcionMenuTienda = self.__menu_de_la_tienda()

            # MOSTRAR PRODUCTOS DE LA TIENDA
            if opcionMenuTienda == 1: 

                # Codigo del producto
                codigoDelProducto = self.__productos_de_la_tienda()

                # Detalle del producto
                if codigoDelProducto != 0: 
                    # Unidades que desea comprar
                    unidadesAComprar = self.__detalle_del_producto(codigoDelProducto)
                    if unidadesAComprar != 0:
                        self.__comprar_producto(codigoDelProducto, unidadesAComprar)

            # MOSTRAR TODAS LAS COMPRAS
            elif opcionMenuTienda == 2:
                opcionMenuTienda = None
                self.__productos_comprados_del_cliente()

            # CERRAR SESION = 3
            elif opcionMenuTienda == 3: 
                return 3

            # SALIR = 0
            else: 
                return 0

    """ 
        SECCION DEL CLIENTE
    """
    def __menu_principal(self)->int:
        return self.__viewConsola.mostrar_menu('Menu Principal', {
            '1':'Iniciar sesion',
            '2':'Registrarse',
            '':'',
            '0':'Salir'
        })
        
    def __menu_de_la_tienda(self)->int:
        return self.__viewConsola.mostrar_menu('Menu de la Tienda',{
            '1':'Ver Productos',
            '2':'Mis compras',
            '':'',
            '3':'Cerrar Sesion',
            '0':'salir'
        })

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
    
    def __productos_comprados_del_cliente(self):
        self.__viewConsola.limpiar_consola()

        comprasUsuario = Compra()
        comprasUsuario.set_usuario_id(self.__usuarioLogeado.get_id())
        compras = comprasUsuario.get_all_for_usuario_id()

        if len(compras) == 0:
            self.__viewConsola.mostrar_mensaje('*************************************')
            self.__viewConsola.mostrar_mensaje('***** NO REALIZO NINGUNA COMPRA *****')
            self.__viewConsola.mostrar_mensaje('*************************************')
            self.__viewConsola.limpiar_consola(2)
        else:
            comprasFormateadas = []
            for compra in compras:
                productoDeLaCompra = Producto().find(compra.get_producto_id())
                compraDict = {
                    'producto' : {
                        'nombre' : productoDeLaCompra.get_nombre(),
                        'precio' : str(productoDeLaCompra.get_precio())
                    },
                    'unidades' : str(compra.get_cantidad()),
                    'precioTotal' : str(compra.get_precioTotal())
                }
                comprasFormateadas.append(compraDict)

            # Muestro todos las compras del usuario
            self.__viewConsola.mostrar_todas_las_compras_del_usuario(comprasFormateadas)
    
    def __detalle_del_producto(self, producto_id):
        producto = Producto().find(producto_id)
        categoriaDelProducto = Categoria().find(producto.get_categoria_id())
        marcaDelProducto = Marca().find(producto.get_marca_id())
        return self.__viewConsola.mostrar_detalle_del_producto({
            'nombre' : producto.get_nombre(),
            'precio' : str(producto.get_precio()),
            'descripcion' : producto.get_descripcion(),
            'categoria' : categoriaDelProducto.get_nombre(),
            'marca' : marcaDelProducto.get_nombre()
        })

    def __comprar_producto(self, producto_id, cantidad):
        producto = Producto().find(producto_id)
        compra = Compra()
        compra.set_cantidad(cantidad)
        compra.set_precioTotal(producto.get_precio()*cantidad)
        compra.set_producto_id(producto_id)
        compra.set_usuario_id(self.__usuarioLogeado.get_id())
        compra.save()
    
    """ 
        SECCION DEL ADMIN
    """
    def __admin_menu_principal(self) -> int:
        return self.__viewConsola.mostrar_menu('Menu principal de Administrador', {
            '1':'Productos',
            '2':'Ventas',
            '3':'Categorias',
            '4':'Marcas',
            '5':'Usuarios',
            '':'',
            '9':'Cerrar Sesion',
            '0':'Salir'
        })

    def __admin_productos_de_la_tienda(self) -> int:
        """ 
            0 => Menu Admin | producto_id => Para Editar 
        """
        productosTienda = Producto().get_all()
        productos = []
        for producto in productosTienda:
            productos.append({
                'id': str(producto.get_id()),
                'nombre': producto.get_nombre(),
                'precio': str(producto.get_precio()),
                'categoria': Categoria().find(producto.get_categoria_id()).get_nombre(),
                'marca': Marca().find(producto.get_marca_id()).get_nombre()
            })
        return self.__viewConsola.admin_mostrar_todos_los_productos(productos)

    def __admin_registro_de_ventas(self):
        ventasDB = Compra().get_all()
        ventas = []
        for venta in ventasDB:
            producto = Producto().find(venta.get_producto_id())
            usuario = Usuario().find(venta.get_usuario_id())
            marca = Marca().find(producto.get_marca_id())
            ventas.append({
                'id' : str(venta.get_id()),
                'unidad' : str(venta.get_cantidad()),
                'precioTotal' : str(venta.get_precioTotal()),
                'producto' : {
                    'id' : str(producto.get_id()),
                    'marca' : marca.get_nombre()
                },
                'usuario' : {
                    'id' : str(usuario.get_id()),
                    'email' : usuario.get_email()
                }
            })

        if len(ventas) == 0:
            self.__viewConsola.mostrar_mensaje('* No se realizo ninguna venta')
            self.__viewConsola.limpiar_consola(1.3)
        else:
            self.__viewConsola.admin_mostrar_todas_las_ventas(ventas, Compra().reporte_de_ventas())

    def __edit_producto_de_la_tienda(self, productoId):
        # Datos del producto
        producto = Producto().find(productoId)
        marcaProducto = Marca().find(producto.get_marca_id())
        categoriaProducto = Categoria().find(producto.get_categoria_id())

        # Categorias
        categorias = []
        for categoria in Categoria().get_all():
            categorias.append({
                'id' : categoria.get_id(),
                'value' : categoria.get_nombre()
            })
        # Marcas
        marcas = []
        for marca in Marca().get_all():
            marcas.append({
                'id' : marca.get_id(),
                'value' : marca.get_nombre()
            })

        nuevoProducto = self.__viewConsola.admin_editar_producto(
            {
                'nombre': producto.get_nombre(),
                'precio' : str(producto.get_precio()),
                'categoria' : categoriaProducto.get_nombre(),
                'marca' : marcaProducto.get_nombre(),
                'descripcion' : producto.get_descripcion()
            },
            categorias,
            marcas
            )

        # Guardar cambios en la DB
        producto.set_nombre(nuevoProducto['nombre'])
        producto.set_precio(nuevoProducto['precio'])
        producto.set_descripcion(nuevoProducto['descripcion'])
        producto.set_categoria_id(nuevoProducto['categoria_id'])
        producto.set_marca_id(nuevoProducto['marca_id'])
        
        if producto.update():
            self.__viewConsola.mostrar_mensaje('\n* Los cambios fueron realizados con exito', 2)
        else:
            self.__viewConsola.mostrar_mensaje('\n* No se pudo realizar el cambio, vuelva a intentar', 2)

    def __admin_mostrar_categorias(self):
        categorias = []
        for categoria in Categoria().get_all():
            categorias.append(
                {
                    'id' : categoria.get_id(),
                    'nombre' : categoria.get_nombre()
                }
            )
        # Mostrar categorias
        self.__viewConsola.admin_mostrar_todas_las_categorias(categorias)

    def __admin_mostrar_marcas(self):
        marcas = []
        for marca in Marca().get_all():
            marcas.append(
                {
                    'id' : marca.get_id(),
                    'nombre' : marca.get_nombre()
                }
            )
        # Mostrar marcas
        self.__viewConsola.admin_mostrar_todas_las_marcas(marcas)

    def __admin_mostrar_usuarios(self):
        usuarios = []
        for usuario in Usuario().get_all(): 
            ciudad = Ciudad().find(usuario.get_ciudad_id())
            usuarios.append({
                'id' : usuario.get_id(),
                'dni' : usuario.get_dni(),
                'nombre' : usuario.get_nombre(),
                'email' : usuario.get_email(),
                'ciudad' : ciudad.get_nombre()
            })
        return self.__viewConsola.admin_mostrar_todos_los_usuarios(usuarios)

    def __admin_eliminar_usuario(self, usuario_id):
        usuario = Usuario().find(usuario_id)
        if  Compra().deleteByUsuarioId(usuario.get_id()) and usuario.delete():
            self.__viewConsola.mostrar_mensaje('* El usuario a sido eliminado correctamente\n* junto con las compras que realizo previamente.',2)
            # Eliminar compras del usuario
        else:
            self.__viewConsola.mostrar_mensaje('* No se pudo eliminar al usuario, vuelva a intentarlo',2)