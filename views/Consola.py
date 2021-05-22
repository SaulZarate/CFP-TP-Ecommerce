import os
import time
from validate_email import validate_email

import pprint

class Consola:

    def __init__(self) -> None:
        self.limpiar_consola()

    def limpiar_consola(self, timer = 0):
        time.sleep(timer)
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

    def mostrar_mensaje(self, message, timer = 0):
        print(message)

    def mostrar_menu(self, titulo, contenido ) -> int:
        while(True): 
            print()
            print('****************************************')
            print('*')
            print('*\t' + titulo.upper() )
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
            self.limpiar_consola(1.5)
    
    """ 
        PRODUCTOS
    """
    def mostrar_todos_los_productos(self, productos) -> int:
        # Opciones validas ( codigos de productos y 0 )
        opcionesValidas = [0]
        for i in productos:
            opcionesValidas.append(i['id'])

        while(True):
            print('**********************************************************************')
            print('*')
            print('*\tPRODUCTOS DE LA TIENDA')
            print('*')
            print('*\tCODIGO\t\tPRECIO\t\tPRODUCTO' )
            for producto in productos:
                print('*\t  ' + str(producto['id']) + '\t\t$' + producto['precio'] + '\t\t' + producto['nombre'])
            print('*')
            print('**********************************************************************')
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
            print('*\tIngrese la cantidad de productos que desee comprar')
            unidades = input('*\tUnidades: ')
            
            try:
                unidadesInt = int(unidades)

                if unidadesInt >= 0 and unidadesInt <= 5:
                    self.limpiar_consola()
                    return unidadesInt
                else:
                    mensaje = '*\t¡¡¡ Solo se pueden comprar 5 productos como maximo !!!'
            except:
                mensaje = '*\t¡¡¡ Solo se permiten numeros enteros !!!'
            print(mensaje)
            self.limpiar_consola(2)

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
        print('*******************************************************************************')
        print('*')
        print('*\t\t\tMIS COMPRAS')
        print('*')
        print('*\tPRECIO\t\tUNIDAD\t\tPRECIO TOTAL\tPRODUCTO' )
        for compra in compras:
            producto = compra['producto']
            print(f'*\t$' + producto['precio'] + '\t\t'+compra['unidades'] + '\t\t$'+compra['precioTotal'] + '\t\t' + producto['nombre'])
        print('*')
        print('*******************************************************************************')
        input('* Ingrese cualquier letra para volver al menu de la tienda: ')
        self.limpiar_consola()

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
    
    def select_formulario(self, datosSolicitado) -> dict:
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
            'name' : 'key del selecet que devuelve'
        }
        """
        opcionesValidas = list( map(lambda option: option['id'], datosSolicitado['values']) )

        print('CIUDADES:')
        for option in datosSolicitado['values']:
            print('Codigo: ' + str(option['id']) + '\tNombre: ' + option['value'] )
        inputUser = input(datosSolicitado['text'] + ': ')
        
        while True:
            try:
                value = int(inputUser.strip())
                if value in opcionesValidas:
                    self.limpiar_consola()
                    return { datosSolicitado['name'] : value}
            except: 
                pass
            inputUser = input('* Valor invalido, vuelva a intentar: ')
