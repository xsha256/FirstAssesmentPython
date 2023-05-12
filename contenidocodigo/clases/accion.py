from abc import ABC, abstractmethod

class Pelicula(ABC):
    def __init__(self, nombre, anyo):
        self.nombre = nombre
        self.anyo = anyo

    @abstractmethod
    def descripcion(self):
        pass

class Accion(Pelicula):
    def __init__(self, nombre, anyo, protagonista):
        super().__init__(nombre, anyo)
        self.protagonista = protagonista

    def descripcion(self):
        print(f"La película de acción '{self.nombre}', estrenada en {self.anyo}, cuenta con el protagonismo de {self.protagonista}. Es una película emocionante y llena de acción.")