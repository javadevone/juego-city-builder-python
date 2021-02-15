from maquinaEstados.InterfazEstadoJuego import InterfazEstadoJuego
from elementosMapa.Cuadro import Cuadro
from elementosMapa.Edificio import Edificio

class EstadoJuego(InterfazEstadoJuego):

    def __init__(self, lienzo):
        self.pixelInicialCanvas = 1
        self.pixelesCuadro = 32
        self.cuadrosHorizontales = int(lienzo.winfo_reqwidth() / self.pixelesCuadro)
        self.cuadrosVerticales = int(lienzo.winfo_reqheight() / self.pixelesCuadro)

        self.lienzo = lienzo
        self.cuadros = []
        self.edificios = []

        self.oro = 1000
        self.piedra = 1000
        self.madera = 1000

        borde = "#009c08"
        relleno = "#009c08"
        bordeResaltado = "#fff"

        for y in range(self.cuadrosVerticales):
            for x in range(self.cuadrosHorizontales):
                xInicial = x * self.pixelesCuadro + self.pixelInicialCanvas
                yInicial = y * self.pixelesCuadro + self.pixelInicialCanvas
                xFinal = x * self.pixelesCuadro + self.pixelesCuadro
                yFinal = y * self.pixelesCuadro + self.pixelesCuadro

                referenciaCuadro = lienzo.create_rectangle(xInicial, yInicial, xFinal, yFinal, fill=relleno, outline=borde, activeoutline=bordeResaltado)
                self.lienzo.tag_bind(referenciaCuadro, '<ButtonPress-1>', self.eventoClick)
                cuadro = Cuadro(xInicial, yInicial, self.pixelesCuadro, relleno, borde, bordeResaltado, referenciaCuadro)
                self.cuadros.append(cuadro)

        print(len(self.cuadros))

    def eventoClick(self, event):
        #print('Clicado', event.x, event.y, event.widget)
        #print(event.widget.find_withtag('current')[0])
        idClicado = event.widget.find_withtag('current')[0]
        print(idClicado)

        if any(x.referenciaLienzo == idClicado for x in self.cuadros):
            print('click en la hierba')
            cuadroClicado = self.obtenerCuadro(idClicado)

            xInicial = cuadroClicado.x
            yInicial = cuadroClicado.y
            xFinal = cuadroClicado.x + self.pixelesCuadro
            yFinal = cuadroClicado.y + self.pixelesCuadro

            relleno = '#ff0000'

            referenciaEdificio = self.lienzo.create_rectangle(xInicial, yInicial, xFinal, yFinal, fill=relleno)
            self.lienzo.tag_bind(referenciaEdificio, '<ButtonPress-1>', self.eventoClick)
            edificio = Edificio("HQ", "HQ", 0, 0, 0, relleno, referenciaEdificio)
            self.edificios.append(edificio)

        if any(x.referenciaLienzo == idClicado for x in self.edificios):
            print('click en un edificio')
            self.lienzo.delete(idClicado)
            self.eliminarEdificio(idClicado)

    def obtenerCuadro(self, referenciaLienzo):
        if any(x.referenciaLienzo == referenciaLienzo for x in self.cuadros):
            for c in range(len(self.cuadros)):
                if self.cuadros[c].referenciaLienzo == referenciaLienzo:
                    return self.cuadros[c]

    def obtenerEdificio(self, referenciaLienzo):
        if any(x.referenciaLienzo == referenciaLienzo for x in self.edificios):
            for e in range(len(self.edificios)):
                if self.edificios[e].referenciaLienzo == referenciaLienzo:
                    return self.edificios[e]

    def eliminarEdificio(self, referenciaLienzo):
        if any(x.referenciaLienzo == referenciaLienzo for x in self.edificios):
            for e in range(len(self.edificios)):
                if self.edificios[e].referenciaLienzo == referenciaLienzo:
                    del self.edificios[e]
                    break

    def actualizar(self):
        m = 2+2

    def dibujar(self):
        z = 2+2