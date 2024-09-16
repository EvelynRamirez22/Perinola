import pytest

from clases.Jugador import Jugador

# Test para agregar jugadores
def test_agregar_jugador():
    ronda = ronda()
    jugador = Jugador("Jugador1", 10)
    
    ronda.agregarJugador(jugador)
    
    assert len(ronda.jugadores) == 1
    assert ronda.jugadores[0] == jugador

# Test para agregar un jugador con 0 o menos fichas
def test_agregar_jugador_no_fichas():
    ronda = ronda()
    jugador = Jugador("Jugador2", 0)
    
    with pytest.raises(ValueError, match="El jugador no puede tener 0 o menos fichas."):
        ronda.agregarJugador(jugador)

# Test para sacar jugadores sin fichas
def test_sacar_jugadores_sin_fichas():
    ronda = ronda()
    jugador1 = Jugador("Jugador1", 10)
    jugador2 = Jugador("Jugador2", 0)
    
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    
    ronda.sacarJugadoresSinFichas()
    
    assert len(ronda.jugadores) == 1
    assert ronda.jugadores[0] == jugador1

# Test para obtener el jugador en turno
def test_jugador_en_turno():
    ronda = ronda()
    jugador = Jugador("Jugador1", 10)
    
    ronda.agregarJugador(jugador)
    
    assert ronda.jugadorEnTurno() == jugador

# Test para obtener el jugador en turno cuando no hay jugadores
def test_jugador_en_turno_sin_jugadores():
    ronda = ronda()
    
    with pytest.raises(IndexError, match="No hay jugadores en la ronda."):
        ronda.jugadorEnTurno()

# Test para pasar el turno
def test_pasar_turno():
    ronda = ronda()
    jugador1 = Jugador("Jugador1", 10)
    jugador2 = Jugador("Jugador2", 15)
    
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    
    ronda.pasarTurno()
    
    assert ronda.jugadorEnTurno() == jugador2

# Test para pasar el turno cuando no hay jugadores
def test_pasar_turno_sin_jugadores():
    ronda = ronda()
    
    with pytest.raises(IndexError, match="No hay jugadores en la ronda."):
        ronda.pasarTurno()

# Test para verificar si queda un solo jugador
def test_queda_un_solo_jugador():
    ronda = ronda()
    jugador1 = Jugador("Jugador1", 10)
    jugador2 = Jugador("Jugador2", 15)
    
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    
    assert not ronda.quedaUnSoloJugador()
    
    ronda.pasarTurno()  # Jugador1 se mueve al final
    ronda.pasarTurno()  # Jugador2 se mueve al final
    ronda.pasarTurno()  # Jugador1 se mueve al final
    ronda.pasarTurno()  # Jugador2 se mueve al final
    ronda.pasarTurno()  # Jugador1 se mueve al final
    
    ronda.sacarJugadoresSinFichas()  # Limpiar jugadores sin fichas
    
    assert ronda.quedaUnSoloJugador()

# Test para el método __str__
def test_str_metodo():
    ronda = ronda()
    jugador1 = Jugador("Jugador1", 10)
    jugador2 = Jugador("Jugador2", 15)
    
    ronda.agregarJugador(jugador1)
    ronda.agregarJugador(jugador2)
    
    assert str(ronda) == "Jugador1 (10 fichas)\nJugador2 (15 fichas)"
    
    ronda.sacarJugadoresSinFichas()
    
    assert str(ronda) == "Jugador1 (10 fichas)\nJugador2 (15 fichas)"
    
    ronda.pasarTurno()
    
    assert str(ronda) == "Jugador2 (15 fichas)\nJugador1 (10 fichas)"
