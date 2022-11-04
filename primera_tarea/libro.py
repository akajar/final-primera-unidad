class Libro:
    id = 0
    
    def __init__(self, 
                 titulo: str, 
                 genero: str, 
                 isbn: str, 
                 editorial: str, 
                 *autores
                 ) -> None:
        self.__titulo = titulo
        self.__genero = genero
        self.__isbn = isbn
        self.__editorial = editorial
        self.__autores = autores
        self.__id = id
        id += 1 #id autoincrementable
    
    def listar(self) -> None:
        #imprime los campos titulo,genero,isbn,editorial,autores
        pass
    
    