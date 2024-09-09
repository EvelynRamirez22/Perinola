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