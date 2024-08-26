from random import choice, random

class Perinola:
    def __init__(self):
        self.caras = ["Pon 1", "Pon 2", "Toma 1", "Toma 2", "Todos Toman", "Ponen Todos"]
        self.cara_visible = "Pon 1"

    def __repr__(self):
        return f"Salió: {self.cara_visible}"

    def tirar(self):
        self.cara_visible = choice(self.caras)
        return self.cara_visible
    




