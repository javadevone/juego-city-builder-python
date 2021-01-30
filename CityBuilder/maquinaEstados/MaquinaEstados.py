from maquinaEstados.EnumEstadosJuego import EnumEstadosJuego
from maquinaEstados.EstadoJuego import EstadoJuego

class MaquinaEstados:
    def __init__(self, estadoInicial, lienzo):
        self.estadoActual = None

        self.cambiarEstado(estadoInicial, lienzo)

    def cambiarEstado(self, nuevoEstado, lienzo):
        if nuevoEstado == EnumEstadosJuego.ESTADO_JUEGO:
            self.estadoActual = EstadoJuego(lienzo)

        if self.estadoActual is None:
            raise Exception("No se ha podido iniciar el juego. El estado del juego " + str(nuevoEstado) + " no es válido.")

    def iterar(self, lienzo):
        self.estadoActual.actualizar()
        self.estadoActual.dibujar(lienzo)