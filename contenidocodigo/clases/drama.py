from abc import ABC, abstractmethod


class Pelicula(ABC):
    def __init__(self, nombre, anyo):
        self.nombre = nombre
        self.anyo = anyo

    @abstractmethod
    def descripcion(self):
        pass


class Drama(Pelicula):
    def __init__(self, nombre, anyo, tema):
        super().__init__(nombre, anyo)
        self.tema = tema

    def descripcion(self):
        return (f"La película dramática '{self.nombre}', estrenada en {self.anyo}, trata el tema de {self.tema}. Es una película emotiva y profunda.")
