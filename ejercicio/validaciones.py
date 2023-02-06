import re
import datetime

class Validaciones:

    def __init__(self):
        pass
    def validateName(self, nombre):
        if len(nombre) < 3 or len(nombre) > 50:
            raise ValueError(f'El nombre debe tener como mínimo 3 caractares y un máximo de 50 caracteres, tamaño actual: {len(nombre)}')
        return True
    def validatePrecio(self, precio):
        if (precio).isdigit() == False:
            raise ValueError(f'El precio debe ser un número')
        return True