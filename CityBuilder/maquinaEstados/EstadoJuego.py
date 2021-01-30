from maquinaEstados.InterfazEstadoJuego import InterfazEstadoJuego

class EstadoJuego(InterfazEstadoJuego):

    def __init__(self, lienzo):
        self.pixelInicialCanvas = 1
        self.pixelesCuadro = 32
        self.cuadrosHorizontales = int(lienzo.winfo_reqwidth() / self.pixelesCuadro)
        self.cuadrosVerticales = int(lienzo.winfo_reqheight() / self.pixelesCuadro)

        self.cuadros = []

        borde = "#009c08"
        relleno = "#009c08"
        bordeResaltado = "#fff"

        for y in range(self.cuadrosVerticales):
            for x in range(self.cuadrosHorizontales):
                xInicial = x * self.pixelesCuadro + self.pixelInicialCanvas
                yInicial = y * self.pixelesCuadro + self.pixelInicialCanvas
                xFinal = x * self.pixelesCuadro + self.pixelesCuadro
                yFinal = y * self.pixelesCuadro + self.pixelesCuadro

                cuadro = lienzo.create_rectangle(xInicial, yInicial, xFinal, yFinal, fill=relleno, outline=borde, activeoutline=bordeResaltado)
                self.cuadros.append(cuadro)

        print(len(self.cuadros))

    def actualizar(self):
        m = 2+2

    def dibujar(self, lienzo):
        z = 2+2