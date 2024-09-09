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
    
  
    
