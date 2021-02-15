from abc import ABC, abstractmethod

class InterfazEstadoJuego(ABC):

    @abstractmethod
    def actualizar(self):
        pass

    @abstractmethod
    def dibujar(self):
        pass