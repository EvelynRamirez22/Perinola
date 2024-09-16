import pytest

# Define la clase Apuesta aquí o importa desde el módulo correspondiente
class Apuesta:
    def __init__(self):
        self.fichas = 0

    def __repr__(self):
        return f"Apuesta: {self.fichas} fichas"

    def ponerFicha(self, cuantas=1):
        if cuantas > 0:
            self.fichas += cuantas

    def tomarFicha(self, cuantas=1):
        if cuantas > 0:
            if cuantas <= self.fichas:
                self.fichas -= cuantas
            else:
                raise ValueError("No hay suficientes fichas para quitar.")
        else:
            print("La cantidad de fichas debe ser positiva.")

    def tomarTodas(self):
        cantidad = self.fichas
        self.fichas = 0
        return cantidad

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas

    def estaVacia(self):
        return self.fichas == 0

# Pruebas para la clase Apuesta
def test_inicializacion():
    apuesta = Apuesta()
    assert apuesta.fichas == 0

def test_ponerFicha():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    assert apuesta.fichas == 5

    apuesta.ponerFicha()
    assert apuesta.fichas == 6

    apuesta.ponerFicha(-3)
    assert apuesta.fichas == 6

def test_tomarFicha():
    apuesta = Apuesta()
    apuesta.ponerFicha(10)
    apuesta.tomarFicha(4)
    assert apuesta.fichas == 6

    with pytest.raises(ValueError):
        apuesta.tomarFicha(7)

    # Prueba para la cantidad negativa en tomarFicha
    apuesta.tomarFicha(-2)
    assert apuesta.fichas == 6

def test_tomarTodas():
    apuesta = Apuesta()
    apuesta.ponerFicha(10)
    fichas_quitadas = apuesta.tomarTodas()
    assert fichas_quitadas == 10
    assert apuesta.fichas == 0

def test_tieneFicha():
    apuesta = Apuesta()
    apuesta.ponerFicha(5)
    assert apuesta.tieneFicha(3) is True
    assert apuesta.tieneFicha(6) is False

def test_estaVacia():
    apuesta = Apuesta()
    assert apuesta.estaVacia() is True
    apuesta.ponerFicha(1)
    assert apuesta.estaVacia() is False
