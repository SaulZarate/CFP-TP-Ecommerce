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

import pprint

class AppController:
    
    def __init__(self):
        self.__usuarioLogeado = None
        self.__viewConsola = Consola()

    def iniciar(self):
        opcionMenuPrincipal = None
        opcionMenuTienda = None
        opcionMenuProductos = None

        while True:
            opcionMenuPrincipal = self.__menu_principal() if opcionMenuPrincipal == None else opcionMenuPrincipal 

            if opcionMenuPrincipal == 1: # ------------ INICIO DE SESION ------------
                if self.__iniciar_sesion() == 0: # registrarse
                    opcionMenuPrincipal = 2
                    continue
                
                """ MENU DE LA TIENDA """
                opcionMenuTienda = self.__menu_de_la_tienda() if opcionMenuTienda == None else opcionMenuTienda

                if opcionMenuTienda == 1: # -------- VER TODOS LOS PRODUCTOS
                    opcionMenuProductos = self.__productos_de_la_tienda() if opcionMenuProductos == None else opcionMenuProductos

                    if opcionMenuProductos == 0: # ---- IR AL MENU DE LA TIENDA
                        opcionMenuTienda = None
                        continue

                elif opcionMenuTienda == 2: # -------- VER MIS COMPRAS
                    print('Mis compras')

                elif opcionMenuTienda == 3: # -------- CERRAR SESION
                    self.__usuarioLogeado = None
                    opcionMenuPrincipal = None
                    continue
                else: # -------- SALIR DE LA APP
                    break

            elif opcionMenuPrincipal == 2: # ------------ REGISTRAR USUARIO ------------
                self.__registrar_usuario()
                # Lo redirijo al menu principal
                opcionMenuPrincipal = None

            else:  # ------------ SALIR DE LA APP ------------
                break
            #self.__productos_de_la_tienda()
        
        # SALIR DE LA APLICACION
    
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
        self.__viewConsola.mostrar_mensaje('* INICIAR SESION ')
        usuario = Usuario()
        while True:
            self.__viewConsola.limpiar_consola()
            inputsUsuario = self.__viewConsola.inputs_formulario([
                { 'text' : 'Ingrese su email', 'type' : 'email', 'name' : 'email' },
                { 'text' : 'Ingrese su contraseña', 'type' : 'str', 'name' : 'clave' }
            ])
            usuario.set_email(inputsUsuario['email'])
            usuario.set_clave(inputsUsuario['clave'])
            
            result = usuario.iniciar_sesion()
            if not usuario.existe_email() :
                mensaje = '* El email ingresado no esta registrado, vuelva a intentarlo.'
            elif result == None:
                mensaje = '* Contraseña incorrecta'
            else:
                self.__viewConsola.limpiar_consola()
                self.__usuarioLogeado = result
                return result

            self.__viewConsola.mostrar_mensaje(mensaje)
            salir =  input('Desea volver al menu principal ? si/no: ')
            if salir == 'si': 
                self.__viewConsola.limpiar_consola()
                return 0


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
    