from enum import Enum, unique
@unique

class EnumEstadosJuego(Enum):
    ESTADO_PANTALLA_TITULO = 0
    ESTADO_MENU_INICIAL = 1
    ESTADO_JUEGO = 2
    ESTADO_MENU_PAUSA = 3