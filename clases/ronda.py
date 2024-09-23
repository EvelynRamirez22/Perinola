class Ronda:

    def __init__(self):
        self.jugadores = [0]

    def __str__(self):
        return "\n".join(str(jugador) for jugador in self.jugadores)

    def agregarJugador(self, jugador):
        if jugador.fichas > 0:
            self.jugadores.append(jugador)
        else:
            raise ValueError("El jugador debe tener fichas para ser agregado.")

    def sacarJugadoresSinFichas(self):
        self.jugadores = [jugador for jugador in self.jugadores if not jugador.sinFichas()]

    def jugadorEnTurno(self):
        if self.jugadores:
            return self.jugadores[0]
        else:
            raise IndexError("No hay jugadores en la ronda.")

    def pasarTurno(self):
        if self.jugadores:
            jugador = self.jugadores.pop(0)
            self.jugadores.append(jugador)
        else:
            raise IndexError("No hay jugadores en la ronda.")

    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1

