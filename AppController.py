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
        opcionMenuPrincipal = None # Login, registro y salir
        opcionMenuTienda = None # Ver productos, compras, cerrar sesion o salir
        codigoDelProducto = None # Detalle del producto o volver al menu de la tienda
        unidadesAComprar = None # Unidades o volver al menu de la tienda

        while True:
            opcionMenuPrincipal = self.__menu_principal() if opcionMenuPrincipal == None else opcionMenuPrincipal 

            if opcionMenuPrincipal == 1: # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> INICIO DE SESION 

                """ -------------------------- """
                """ ---- INICIO DE SESION ---- """
                """ -------------------------- """
                if self.__usuarioLogeado == None:
                    if self.__iniciar_sesion() == 0: # registrarse
                        opcionMenuPrincipal = 2
                        continue

                """ --------------------------- """
                """ ---- MENU DE LA TIENDA ---- """
                """ --------------------------- """
                if opcionMenuTienda == None: 
                    opcionMenuTienda = self.__menu_de_la_tienda()


                # ---------------------------------
                # ---- VER TODOS LOS PRODUCTOS ----
                # ---------------------------------
                if opcionMenuTienda == 1: 
                    # codigo del producto o 0 para volver al menu de la tienda
                    if codigoDelProducto == None:
                        codigoDelProducto = self.__productos_de_la_tienda()

                    # ------------------------------
                    # ---- Detalle del producto ----
                    # ------------------------------
                    if codigoDelProducto != 0: 
                        # Unidades que desea comprar
                        unidadesAComprar = self.__detalle_del_producto(codigoDelProducto)
                        if unidadesAComprar != 0:
                            self.__comprar_producto(codigoDelProducto, unidadesAComprar)
                    
                    opcionMenuPrincipal = 1
                    opcionMenuTienda = None
                    codigoDelProducto = None
                    unidadesAComprar = None
                    continue

                # -------------------------
                # ---- VER MIS COMPRAS ----
                # -------------------------
                elif opcionMenuTienda == 2:
                    opcionMenuTienda = None
                    self.__productos_comprados_del_cliente()


                # -----------------------
                # ---- CERRAR SESION ----
                # -----------------------
                elif opcionMenuTienda == 3: 
                    self.__usuarioLogeado = None
                    opcionMenuPrincipal = None
                    opcionMenuTienda = None
                    codigoDelProducto = None
                    continue
                
                # --------------------
                # ---- CERRAR APP ---- 
                # --------------------
                else: 
                    break

            elif opcionMenuPrincipal == 2: # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> REGISTRAR USUARIO 
                self.__registrar_usuario()
                # Lo redirijo al menu principal
                opcionMenuPrincipal = None

            else:  # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~> CERRAR APP 
                break
        
        # CERRAR APP
    
    def pruebas(self):
        self.__seccion_del_cliente()
        #self.__seccion_del_administrador()

    """ 
        INICIO DE SESION & REGISTRO 
    """
    def __menu_principal(self)->int:
        return self.__viewConsola.mostrar_menu('Menu Principal', {
            '1':'Iniciar sesion',
            '2':'Registrarse',
            '':'',
            '0':'salir'
        })
    
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
        self.__viewConsola.mostrar_mensaje('* Usuario registrado correctamente, ahora puede iniciar sesion.')
        self.__viewConsola.limpiar_consola(5)

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
            'name': 'ciudad_id'
        })
        inputsUsuario.update(ciudadElegida)
        return inputsUsuario

    def __iniciar_sesion(self) -> Usuario:
        self.__viewConsola.limpiar_consola()
        self.__viewConsola.mostrar_mensaje('***************************')
        self.__viewConsola.mostrar_mensaje('**** INICIAR DE SESION ****')
        self.__viewConsola.mostrar_mensaje('***************************\n')
        usuario = Usuario()
        while True:
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
        ADMINISTRADOR & CLIENTE
    """
    def __seccion_del_administrador(self) -> int:
        """ 
            return 0 = salir de la App
            return 1 = cerrar sesion
        """
        return None

    def __seccion_del_cliente(self) -> int:
        """ 
            return 0 = salir de la App
            return 1 = cerrar sesion
        """
        opcionMenuTienda = None 
        codigoDelProducto = None 
        unidadesAComprar = None 
        while True:
            # MENU PRINCIPAL
            if opcionMenuTienda == None:
                opcionMenuTienda = self.__menu_de_la_tienda()

            # ---------------------------------
            # ---- VER TODOS LOS PRODUCTOS ----
            # ---------------------------------
            if opcionMenuTienda == 1: 
                # codigo del producto o 0 para volver al menu de la tienda
                if codigoDelProducto == None:
                    codigoDelProducto = self.__productos_de_la_tienda()

                # ------------------------------
                # ---- Detalle del producto ----
                # ------------------------------
                if codigoDelProducto != 0: 
                    # Unidades que desea comprar
                    unidadesAComprar = self.__detalle_del_producto(codigoDelProducto)
                    if unidadesAComprar != 0:
                        self.__comprar_producto(codigoDelProducto, unidadesAComprar)
                
                opcionMenuPrincipal = 1
                opcionMenuTienda = None
                codigoDelProducto = None
                unidadesAComprar = None
                continue

            # -------------------------
            # ---- VER MIS COMPRAS ----
            # -------------------------
            elif opcionMenuTienda == 2:
                opcionMenuTienda = None
                self.__productos_comprados_del_cliente()


            # -----------------------
            # ---- CERRAR SESION ----
            # -----------------------
            elif opcionMenuTienda == 3: 
                self.__usuarioLogeado = None
                opcionMenuPrincipal = None
                opcionMenuTienda = None
                codigoDelProducto = None
                continue
            
            # --------------------
            # ---- CERRAR APP ---- 
            # --------------------
            else: 
                break

    """ 
        TIENDA
    """
    def __menu_de_la_tienda(self)->int:
        return self.__viewConsola.mostrar_menu('Menu de la Tienda',{
            '1':'Ver los Productos de la tienda',
            '2':'Ver mis compras',
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
