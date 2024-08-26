

class Apuesta:
    def __init__(self):
        self.fichas = 0

    def ponerFicha(self, cuantas=1):

        if cuantas > 0:
            self.fichas += cuantas
        else:
            raise ValueError("La cantidad de fichas a agregar debe ser positiva.")

    def tomarFicha(self, cuantas=1):

        if cuantas > 0:
            if cuantas <= self.fichas:
                self.fichas -= cuantas
            else:
                raise ValueError("No hay suficientes fichas para tomar.")
        else:
            raise ValueError("La cantidad de fichas a quitar debe ser positiva.")

    def tomarTodas(self):

        todas = self.fichas
        self.fichas = 0
        return todas

    def tieneFicha(self, cuantas=1):

        return self.fichas >= cuantas

    def estaVacia(self):

        return self.fichas == 0

    def __repr__(self):

        return f"Apuesta: {self.fichas} fichas"