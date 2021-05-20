import os
import time

class Menu:

    def __limpiar_consola(self):
        clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
        clearConsole()

    def mostrar_menu(self, titulo, contenido ) -> int:
        self.__limpiar_consola()
        while(True): 
            print()
            print('****************************************')
            print('*')
            print('*\t' + titulo.upper() )
            for key, value in contenido.items():
                print('*\t' + key + '- ' + value)
            print('*')
            print('****************************************')
            opcion = input('*\tOpcion: ')
            print('*')
            try:
                opcionElegida = int(opcion)
                if opcionElegida in contenido.keys():
                    self.__limpiar_consola()
                    return opcionElegida
            except:
                pass
            print('*\t¡¡¡ Opcion invalida !!!')
            print('*')
            print('****************************************')
            time.sleep(1.5)
            self.__limpiar_consola()
    
    def mostrar_productos(self,titulo,productos):
        self.__limpiar_consola()
        print('********************************************************************************')
        print('*')
        print('*\t' + titulo.upper() )
        print('*')
        print('*\tPRODUCTOS\t\t\t\t\tPRECIOS' )
        for producto in productos:
            for precio, nombre in producto.items():
                print('*\t' + nombre + '\t\t\t\t$' + precio)
        print('*')
        print('********************************************************************************')