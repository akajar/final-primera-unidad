import config

class Libro:
    
    def __init__(self):
        self.id = ''
        self.titulo = ''
        self.genero = ''
        self.isbn = ''
        self.editorial = ''
        self.autores = ''
        self.libros_general = []
    
    # Menu del sistema
    def main(self):
        config.imprimir_menu_libros()
        opcion = config.mensaje_opcion('Ingrese una opcion para la operacion a realizar')
        