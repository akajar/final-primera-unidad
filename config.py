import os
import requests
from colorama import Fore

def mensaje_opcion(mensaje:str)->int:
    valor=""
    while True:
        valor = input(Fore.CYAN+mensaje+' !# '+Fore.RESET)
        if valor != '' and valor.isnumeric():
            break
        else:
            imprimir_errores('Opcion no es valida, Ingrese un numero')
            valor = input(Fore.CYAN+mensaje+' !# '+Fore.RESET)
    return int(valor)

def imprimir_menu_libros():
    os.system('clear')
    print('''    ===================================
    |        CONFIGURA LIBROS         |
    ===================================
    |  1: Leer archivo.               |
    |  2: Listar libros.              |
    |  3: Agregar libros.             |
    |  4: Eliminar libro.             |
    |  5: Buscar libros.              |
    |  6: Ordenar libros por título.  |
    |  7: Editar datos de un libro.   |
    |  8: Guardar libro.              |
    |  9: Salir.                      |
    ===================================''')