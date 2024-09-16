import pytest

# Define la clase Jugador aquí o importa desde el módulo correspondiente
class Jugador:
    def __init__(self, nombre, fichas=5):
        self.nombre = nombre
        self.fichas = fichas

    def __str__(self):
        return f"{self.nombre}, {self.fichas} fichas"

    def darFicha(self, cuantas=1):
        if cuantas > 0:
            self.fichas += cuantas
        else:
            print("La cantidad de fichas debe ser positiva.")

    def sacarFicha(self, cuantas=1):
        if cuantas > 0:
            if cuantas <= self.fichas:
                self.fichas -= cuantas
            else:
                raise ValueError("No tienes suficientes fichas para sacar.")
        else:
            print("La cantidad de fichas debe ser positiva.")

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas

    def sinFichas(self):
        return self.fichas == 0

# Pruebas para la clase Jugador
def test_inicializacion():
    jugador = Jugador("Carlos")
    assert jugador.nombre == "Carlos"
    assert jugador.fichas == 5

def test_darFicha():
    jugador = Jugador("Carlos")
    jugador.darFicha(3)
    assert jugador.fichas == 8

    jugador.darFicha()
    assert jugador.fichas == 9

    # No debería cambiar el número de fichas si se intenta agregar una cantidad negativa
    jugador.darFicha(-2)
    assert jugador.fichas == 9

def test_sacarFicha():
    jugador = Jugador("Carlos")
    jugador.sacarFicha(2)
   
