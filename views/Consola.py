import os
import time

class Consola:

    def __limpiar_consola(self, timer = 0):
        time.sleep(timer)
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

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
                    print('*\t' + key + '- ' + value)
            print('*')
            print('****************************************')
            opcion = input('*\tOpcion: ')
            print('*')
            try:
                opcionElegida = int(opcion)
                if str(opcionElegida) in contenido.keys():
                    self.__limpiar_consola()
                    return int(opcionElegida)
            except:
                pass
            print('*\t¡¡¡ Opcion invalida !!!')
            print('*')
            print('****************************************')
            self.__limpiar_consola(1.5)
    
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
                    self.__limpiar_consola(1)
                    return opcionElegida
            except:
                pass
            print('*\t¡¡¡ Opcion invalida !!!')
            print('*')
            print('****************************************')
            self.__limpiar_consola(1.5)
    
    def inputs_formulario(self, datosSolicitados) -> dict:
        resultados = {}
        while True:
            for dato in datosSolicitados:
                inputUser = input(dato['text'] + ': ')
                try:
                    if dato['type'] == 'int':
                        value = int(value)
                    elif dato['type'] == 'float':
                        value = float(value)
                    resultados[dato['name']] = inputUser
                except:
                    resultados={}
                    break
            if resultados == {}:
                print()
                print('\t¡¡¡Ingreso un dato invalido, vuelva a intentarlo!!!')
                self.__limpiar_consola(1.5)
            else:
                return resultados
    
    def select_formulario(self, datosSolicitado) -> dict:
        """ 
        {
            'values' : []
            'text' : ...
            'type' : ...
            'name' : ...
        }
        """
        while True:
            inputUser = input(datosSolicitado['text'] + ': ')
            try:
                value = None
                if datosSolicitado['type'] == 'int':
                    value = int(inputUser)
                if datosSolicitado['type'] == 'float':
                    value = int(inputUser)
                if value in datosSolicitado['values']:
                    self.__limpiar_consola()
                    return value
            except: 
                pass
            print('******** Valor incorrecto, vuelva a intentar ********')
            print()
