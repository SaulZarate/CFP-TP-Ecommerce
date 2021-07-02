import os
import time
from validate_email import validate_email

class Consola:

    def __init__(self) -> None:
        self.limpiar_consola()

    def limpiar_consola(self, timer = 0):
        time.sleep(timer)
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

    def mostrar_mensaje(self, message, timer = 0):
        print(message)
        if timer != 0:
            self.limpiar_consola(timer)

    def mostrar_menu(self, titulo, contenido ) -> int:
        while(True): 
            print()
            print('****************************************')
            print('*')
            print('*\t' + titulo.upper() )
            print('*')
            for key, value in contenido.items():
                if key == '' or value == '':
                    print('*')
                else:
                    print('*\t' + key + '. ' + value)
            print('*')
            print('****************************************')
            opcion = input('*\tOpcion: ')
            print('*')
            try:
                opcionElegida = int(opcion)
                if str(opcionElegida) in contenido.keys():
                    self.limpiar_consola()
                    return int(opcionElegida)
            except:
                pass
            print('*\t¡¡¡ Opcion invalida !!!')
            print('*')
            print('****************************************')
            self.limpiar_consola(1.3)

    """ 
        PRODUCTOS
    """
    def mostrar_todos_los_productos(self, productos) -> int:
        # Opciones validas ( codigos de productos y 0 )
        opcionesValidas = [0]
        for i in productos:
            opcionesValidas.append(i['id'])

        while(True):
            print('******************************************************************************************')
            print('*')
            print('*\tPRODUCTOS DE LA TIENDA')
            print('*')
            print('*\tCODIGO\t\tPRECIO\t\tPRODUCTO' )
            for producto in productos:
                print('*\t  ' + str(producto['id']) + '\t\t$' + producto['precio'] + '\t\t' + producto['nombre'])
            print('*')
            print('******************************************************************************************')
            print('*\tPara ver un producto ingrese su codigo')
            print('*\tPara volver al menu de la tienda ingrese 0')
            opcion = input('*\tCodigo: ')
            print('*')
            try:
                opcionElegida = int(opcion)
                if opcionElegida in opcionesValidas:
                    self.limpiar_consola()
                    return opcionElegida
            except:
                pass
            print('*\t¡¡¡ Opcion invalida !!!')
            print('*')
            print('****************************************')
            self.limpiar_consola(1.5)
    
    def mostrar_detalle_del_producto(self, producto) -> int:
        """ 
            {
                'nombre' : '...',
                'precio' : '...',
                'descripcion' : '...'
                'categoria' : '...',
                'marca' : '...',
            }
        """
        self.limpiar_consola()
        while True:
            print('**********************************************************************')
            print('*')
            print('*\t' + producto['nombre'].upper())
            print('*')
            print('*\tPrecio: $' + producto['precio'])
            print('*\tCategoria: ' + producto['categoria'])
            print('*\tMarca: ' + producto['marca'])
            print('*\tDescripcion: ' + producto['descripcion'])
            print('*')
            print('**********************************************************************')
            print('*\tIngrese la cantidad de productos que desee comprar. 0 para salir')
            unidades = input('*\tUnidades: ')
            
            try:
                unidadesInt = int(unidades)

                if unidadesInt >= 0 and unidadesInt <= 5:
                    print('* Compra realizada con exito')
                    self.limpiar_consola(1.5)
                    return unidadesInt
                else:
                    mensaje = '*\t¡¡¡ Solo se pueden comprar 5 productos como maximo !!!'
            except:
                mensaje = '*\t¡¡¡ Solo se permiten numeros enteros !!!'
            print(mensaje)
            self.limpiar_consola(2)

    def admin_mostrar_todos_los_productos(self, productos) -> int:
        """ 
            [
                {
                    'id' : '...',
                    'nombre' : '...',
                    'precio' : '...',
                    'categoria' : '...',
                    'marca' : '...',
                },
                ...
            ]
        """
        self.limpiar_consola()
        opcionesValidas = list( map(lambda producto: int(producto['id']), productos) )
        opcionesValidas.append(0)
        while True:
            print('**********************************************************************')
            print('*')
            print('*\tLISTA DE PRODUCTOS')
            print('*')
            print('*\tID\tPRECIO\t\tMARCA\t\tCATEGORIA\tNOMBRE' )
            for producto in productos:
                # PARA LA TABULACION ENTRE MARCA Y CATEGORIA
                if len(producto['marca']) >= 8:
                    print('*\t' + producto['id'] + '\t$' + producto['precio'] + '\t\t' + producto['marca'] + '\t' + producto['categoria'] + '\t\t' + producto['nombre'] )
                else:
                    print('*\t' + producto['id'] + '\t$' + producto['precio'] + '\t\t' + producto['marca'] + '\t\t' + producto['categoria'] + '\t\t' + producto['nombre'] )
            print('*')
            print('**********************************************************************')
            print('*\tPara editar un producto ingrese su ID')
            print('*\tPara salir ingrese 0')
            opcion = input('*\tCodigo: ')
            print('*')
            try:
                opcionElegida = int(opcion)
                if opcionElegida in opcionesValidas:
                    self.limpiar_consola()
                    return opcionElegida
            except:
                pass
            print('*\t¡¡¡ Codigo o ID incorrecto !!!')
            print('*')
            print('****************************************')
            self.limpiar_consola(1.3)

    def admin_editar_producto(self, producto, categorias, marcas) -> int:
        """ 
            producto = {
                'nombre' : '...',
                'precio' : '...',
                'categoria' : '...',
                'marca' : '...'
                'descripcion' : '...',
            },
            categorias = [
                {
                    'id': ...,
                    'nombre' : '...'
                },
                ...
            ],
            marcas = [
                {
                    'id': ...,
                    'nombre' : '...'
                },
                ...
            ]
        """
        self.limpiar_consola()
        print('*************************************************************')
        print('*')
        print('*\t' + producto['nombre'].upper())
        print('*')
        print('*\tPrecio: $' + producto['precio'])
        print('*\tCategoria: ' + producto['categoria'])
        print('*\tMarca: ' + producto['marca'])
        print('*\tDescripcion: ' + producto['descripcion'])
        print('*')
        print('*************************************************************')
        print('\nIngrese los nuevos valores: \n')

        nombre = input('Nombre: ')
        descripcion = input('Descripcion: ')
        while True:
            try:
                precio = input('Precio: ')
                precio = float(precio)

                categoria_id = self.select_formulario({
                    'values' : categorias,
                    'text' : 'Seleccione el Id de la nueva categoria',
                    'name' : 'categoria_id',
                    'title' : 'CATEGORIAS'
                }, False)
                marca_id = self.select_formulario({
                    'values' : marcas,
                    'text' : 'Seleccione el Id de la nueva categoria',
                    'name' : 'marca_id',
                    'title' : 'MARCAS'
                }, False)
                
                return {
                    'nombre' : nombre,
                    'precio' : precio,
                    'descripcion' : descripcion,
                    'categoria_id' : categoria_id['categoria_id'],
                    'marca_id' : marca_id['marca_id']
                }
            except:
                mensaje = '*\t¡¡¡ El precio debe ser un numero !!!'
            print(mensaje)

    """         
        COMPRAS
    """
    def mostrar_todas_las_compras_del_usuario(self, compras):
        """ 
            [{
                'producto' : {
                    'nombre' : '...' ,
                    'precio' : '...'
                },
                'unidades' : '...',
                'precioTotal' : '...'
            },
            ...
            ]
        """
        print('*************************************************************************************************')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\t\t\t\t\t\tMIS COMPRAS\t\t\t\t\t*')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*************************************************************************************************')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\tPRECIO_PRODUCTO\t\tUNIDAD\t\tPRECIO TOTAL\tPRODUCTO\t\t\t*' )
        for compra in compras:
            producto = compra['producto']
            mensaje = '*\t    $' + producto['precio'] + '\t\t  '+compra['unidades'] + '\t\t  $'+compra['precioTotal']
            mensaje += '\t\t' if ( len(compra['precioTotal'])+4 ) < 8 else '\t'
            mensaje += producto['nombre']
            if ( len(producto['nombre'])+1 ) < 8:
                mensaje += '\t\t\t\t*'
            elif ( len(producto['nombre'])+1 ) < 16:
                mensaje += '\t\t\t*'
            elif ( len(producto['nombre'])+1 ) < 24:
                mensaje += '\t\t*'
            else:
                mensaje += '\t*'
            print( mensaje )
        print('*\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*************************************************************************************************')
        input('* Ingrese cualquier letra para volver al menu de la tienda: ')
        self.limpiar_consola()

    def admin_mostrar_todas_las_ventas(self, ventas, datosDeReporte):
        """ 
            [{
                'id' : '...',
                'unidad' : '...',
                'precioTotal' : '...',
                'producto' : {
                    'id' : '...',
                    'marca' : '...'
                },
                'usuario' : {
                    'id' : '...',
                    'email' : '...'
                }
            },
            ...
            ]
        """
        self.limpiar_consola()
        print('*************************************************************************************************************************')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\t\t\t\t\t\tREPORTE DE VENTAS\t\t\t\t\t\t\t*')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*************************************************************************************************************************')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\t Id\tUnidades x\tTotal de\tCodigo del\tMarca del\t   Id\t\t\t\t\t*')
        print('*\tVenta\t Producto\tla venta\t Producto\tProducto\t Usuario\tEmail del usuario\t*')
        #print('*\tId\tUnidad\t\tPrecioVenta\tIdProducto\tMarcaProducto\tIdUsuarios\tEmailUsuarios\t\t*')
        for venta in ventas:
            fila = '*\t  ' + venta['id'] + '\t    ' + venta['unidad'] + '\t\t$' + venta['precioTotal']
            fila += '\t\t    ' if ( len(venta['precioTotal'])+1 ) < 8 else '\t    '
            fila += venta['producto']['id'] + '\t\t' + venta['producto']['marca']
            fila += '\t\t' if len(venta['producto']['marca']) < 8 else '\t'
            fila += '   ' + venta['usuario']['id'] + '\t\t' + venta['usuario']['email']
            fila += '\t\t*' if len(venta['usuario']['email']) < 16 else '\t*'
            print(fila)
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*************************************************************************************************************************')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*\tIngresos: $' + datosDeReporte['ingresos'] + '\tUnidades vendidas: ' + datosDeReporte['unidadesVendidas'] + '\t\tUsuarios activos: ' + datosDeReporte['usuariosActivos'] + '\t\tVentas relizadas: '+ datosDeReporte['ventasRealizadas'] + '\t*')
        print('*\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t*')
        print('*************************************************************************************************************************')
        input('Ingrese cualquier caracter para salir: ')
        self.limpiar_consola()

    """ 
        MARCAS
    """
    def admin_mostrar_todas_las_marcas(self, marcas) -> None:
        """ 
            [
                {
                    'id' : 0,
                    'nombre' : '...'
                },
                ...
                ...
            ]
        """
        self.limpiar_consola()
        print('***********************************************')
        print('*')
        print('*\tMARCAS')
        print('*')
        print('*\tID\tNOMBRE')
        for marca in marcas:
            print(f'*\t{marca["id"]}\t{marca["nombre"]}')
        print('*')
        print('***********************************************')
        input('*\tIngrese cualquier caracter para salir: ')
        self.limpiar_consola()

    """ 
        CATEGORIAS
    """
    def admin_mostrar_todas_las_categorias(self, categorias) -> None:
        """ 
            [
                {
                    'id' : 0,
                    'nombre' : '...'
                },
                ...
                ...
            ]
        """
        self.limpiar_consola()
        print('***********************************************')
        print('*')
        print('*\tCATEGORIAS')
        print('*')
        print('*\tID\tNOMBRE')
        for categoria in categorias:
            print(f'*\t{categoria["id"]}\t{categoria["nombre"]}')
        print('*')
        print('***********************************************')
        input('*\tIngrese cualquier caracter para salir: ')
        self.limpiar_consola()

    """ 
        USUARIOS
    """
    def admin_mostrar_todos_los_usuarios(self, usuarios) -> int:
        """ 
            [
                {
                    'id' : ... ,
                    'dni' : '...' ,
                    'nombre' : '...' ,
                    'email' : '...' ,
                    'ciudad' : '...'
                }
            ]
        """
        opcionesValidas = list(map( lambda u: u['id'], usuarios ))
        opcionesValidas.append(0)

        self.limpiar_consola()
        
        while(True):
            print('***********************************************************************************')
            print('*')
            print('*\tUSUARIOS')
            print('*')
            print('*\tID\tDNI\t\tNOMBRE\t\tCIUDAD\t\tEMAIL' )
            for usuario in usuarios:
                mensaje = '*\t' + str(usuario['id']) + '\t' + usuario['dni'] + '\t' + usuario['nombre'] + '\t\t' +usuario['ciudad']
                if len(usuario['ciudad']) < 8:
                    mensaje += '\t' 
                mensaje += '\t' + usuario['email']
                print(mensaje)

            print('*')
            print('***********************************************************************************')
            print('*\tPara eliminar un usuario ingrese su ID')
            print('*\tPara volver atras ingrese 0')
            opcion = input('*\tOpcion: ')
            print('*')
            try:
                opcionElegida = int(opcion)
                if opcionElegida in opcionesValidas:
                    self.limpiar_consola()
                    return opcionElegida
            except:
                pass
            print('*\t¡¡¡ Opcion invalida !!!')
            print('*')
            print('****************************************')
            self.limpiar_consola(1.5)

    """ 
        FORMULARIOS
    """
    def inputs_formulario(self, datosSolicitados) -> dict:
        """ 
            [
                {
                    'text': 'texto del label', 
                    'type': 'tipo de input (str, int, float)', 
                    'name': 'key del diccionario que devuelve'
                },
                { 
                    ... 
                }
            ]
        """
        resultados = {}
        while True:
            mensaje = ''
            for dato in datosSolicitados:
                inputUser = input(dato['text'] + ': ').strip()
                try:
                    if dato['type'] == 'int':
                        inputUser = int(inputUser)
                        mensaje = '* Solo se permiten numeros enteros'
                    elif dato['type'] == 'float':
                        inputUser = float(inputUser)
                        mensaje = '* Solo se permiten numeros con decimales'
                    elif dato['type'] == 'email' and not validate_email(inputUser):
                        mensaje = '* El email ingresado es invalido'
                        raise Exception('*Email envalido')
                        
                    resultados[dato['name']] = inputUser
                except:
                    resultados={}
                    break
            if resultados == {}:
                print(mensaje)
                self.limpiar_consola(1.5)
            else:
                return resultados
    
    def select_formulario(self, datosSolicitado, limpiarConsola = True) -> dict:
        """ 
        {
            'values' : [
                {
                    id1: int , 
                    value1: str
                },
                {
                    id2: int,
                    value2: str
                }
                ],
            'text' : 'titulo del select' ,
            'name' : 'key del select que devuelve',
            'title' : '...'
        }
        """
        opcionesValidas = list( map(lambda option: option['id'], datosSolicitado['values']) )

        if datosSolicitado["title"] != '':
            print(f'{datosSolicitado["title"]}: ')
        for option in datosSolicitado['values']:
            print('Codigo: ' + str(option['id']) + '\tNombre: ' + option['value'] )
        inputUser = input(datosSolicitado['text'] + ': ')
        
        while True:
            try:
                value = int(inputUser.strip())
                if value in opcionesValidas:
                    if limpiarConsola:
                        self.limpiar_consola()
                    return { datosSolicitado['name'] : value}
            except: 
                pass
            inputUser = input('* Valor invalido, vuelva a intentar: ')
