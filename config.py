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
