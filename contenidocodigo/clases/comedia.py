from abc import ABC, abstractmethod


class Pelicula(ABC):
    def __init__(self, nombre, anyo):
        self.nombre = nombre
        self.anyo = anyo

    @abstractmethod
    def descripcion(self):
        pass


class Comedia(Pelicula):
    def __init__(self, nombre, anyo, director):
        super().__init__(nombre, anyo)
        self.director = director

    def descripcion(self):
        return(f"La comedia '{self.nombre}', estrenada en {self.anyo}, fue dirigida por {self.director}. Es una película divertida y con un buen sentido del humor.")
