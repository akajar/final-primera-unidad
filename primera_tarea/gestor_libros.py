from typing import List
from libro import Libro

class Gestor_libros:
    def __init__(self) -> None:
        self.__ruta_archivo = "libros.csv"
    
    def cargar_archivo(self) -> List[str]:
        #abre el archivo y guarda los libros en memoria
        self.libros = ["libro1","libro2","libro3"] #es un ejemplo
    
    def agregar_libro(self, libro: Libro) -> None:
        #carga un libro en memoria (self.libros)
        self.libros.append(libro)
    
    def eliminar_libro(self,id: int) -> None:
        #elimina un libro, segun su id, de la lista
        pass
    
    #Filtra los libros segun en tipo: 
    #1(id), 2(titulo), 3(autor), 4(editorial), 5(genero)
    def buscar_libro_id(self, clave: int) -> List[Libro]:
        pass
    
    def buscar_libro_titulo(self, clave: str) -> List[Libro]:
        pass
    
    def buscar_libro_autor(self, clave: str) -> List[Libro]:
        pass
    
    def buscar_libro_editorial(self, clave: str) -> List[Libro]:
        pass
    
    def buscar_libro_genero(self, clave: str) -> List[Libro]:
        pass
    
    def ordenar_libros(self) -> None:
        #Ordena la lista segun sus titulos
        pass
    
    def actualizar_libro(self) -> None:
        #Actualiza los datos de un libro
        pass
    
    def grabar_archivo(self) -> None:
        #Graba la lista de libros en el archivo
        pass