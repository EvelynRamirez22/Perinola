class Ronda:
    def __init__(self):
        self.jugadores = []

    def agregarJugador(self, jugador):
        if jugador.fichas <= 0:
            raise ValueError("El jugador no puede tener 0 o menos fichas.")
        self.jugadores.append(jugador)

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if jugador.fichas > 0]

    def jugadorEnTurno(self):
        if not self.jugadores:
            raise IndexError("No hay jugadores en la ronda.")
        return self.jugadores[0]

    def pasarTurno(self):
        if not self.jugadores:
            raise IndexError("No hay jugadores en la ronda.")
        jugador = self.jugadores.pop(0)
        self.jugadores.append(jugador)

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1

    def __str__(self):
        if not self.jugadores:
            return "No hay jugadores en la ronda."
        return "\n".join(str(jugador) for jugador in self.jugadores)