from typing import List
from libro import Libro

class Gestor_libros:
    __ruta_archivo = "libros.csv"
    __libros= []
    
    @classmethod
    def cargar_archivo(cls) -> None:
        #abre el archivo y guarda los libros en memoria
        pass
    
    @classmethod
    def listar_libros(cls) -> None:
        #llama al metodo listar de cada libro en la lista
        pass
    
    @classmethod
    def agregar_libro(cls, **datos) -> None:
        #carga un libro en la lista de libros
        pass
    
    @classmethod
    def eliminar_libro(cls,id: int) -> None:
        #elimina un libro, segun su id, de la lista
        pass
    
    #Filtra los libros segun: 
    @classmethod
    def buscar_libro_isbn(cls, clave: str) -> List[Libro]:
        pass
    
    @classmethod
    def buscar_libro_titulo(cls, clave: str) -> List[Libro]:
        pass
    
    @classmethod
    def buscar_libro_autor(cls, clave: str) -> List[Libro]:
        pass
    
    @classmethod
    def buscar_libro_editorial(cls, clave: str) -> List[Libro]:
        pass
    
    @classmethod
    def buscar_libro_genero(cls, clave: str) -> List[Libro]:
        pass
    
    @classmethod
    def ordenar_libros(cls) -> None:
        #Ordena la lista segun sus titulos
        pass
    
    @classmethod
    def actualizar_libro(cls) -> None:
        #Actualiza los datos de un libro
        pass
    
    @classmethod
    def grabar_archivo(cls) -> None:
        #Graba la lista de libros en el archivo
        pass
    