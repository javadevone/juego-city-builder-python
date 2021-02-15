from tkinter import Tk, Canvas
import time
import sys

from maquinaEstados.MaquinaEstados import MaquinaEstados
from maquinaEstados.EnumEstadosJuego import EnumEstadosJuego

class Ventana:
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
        self.ventana = Tk()
        self.ventana.title("Dungeon manager")
        self.lienzo = Canvas(self.ventana, bg="white", width=self.ancho, height=self.alto)
        self.lienzo.pack()

        self.msPorActualizacion = 16

        self.aps = 0
        self.referenciaInicial = time.perf_counter_ns()

        self.me = MaquinaEstados(EnumEstadosJuego.ESTADO_JUEGO, self.lienzo)
        
        self.ventana.after(0, self.iterar)

        self.ventana.bind("<Key>", self.tecla)

        self.ventana.mainloop()

    def tecla(self, event):
        if event.char == "q":
            print("saliendo del juego")
            sys.exit(0)

    def iterar(self):
        referenciaActual = time.perf_counter_ns()
        nsAcumulados = referenciaActual - self.referenciaInicial

        self.me.iterar()

        if nsAcumulados / 1000000 >= 1000:
            print("APS: " + str(self.aps))
            self.aps = 0
            self.referenciaInicial = time.perf_counter_ns()

        self.ventana.after(self.msPorActualizacion, self.iterar)
        self.aps += 1

v = Ventana(800, 600)