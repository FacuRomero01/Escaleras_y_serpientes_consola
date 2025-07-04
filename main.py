from datos import guarda_puntaje
from preg_random import pregunta
from preguntas import preguntas

tablero = [
        0,  1,  0,  0,  0,  3,  0,  0,  0,  0,
        0,  1,  0,  0,  2,  1,  1,  0,  0,  0,
        1,  0,  0,  2,  0,  0,  0,  1,  0,  0,
        0
]
posicion = 15
puntaje = 0

def aplica_escaleras(posicion) -> int:
    """
    Función que verifica si la posición actual del jugador contiene una escalera y,
    de ser así, aplica el avance correspondiente. En caso contrario, mantiene la misma
    posición.

    El tablero tiene marcadas las escaleras como valores positivos en las posiciones
    donde empiezan. Si hay una escalera, el jugador avanza la cantidad indicada.

    Args:
        posicion (int): Número de casilla donde se encuentra actualmente el jugador.

    Return:
        int: Devuelve la nueva posición del jugador luego de aplicar la escalera (si existe).
            Si no hay escalera, devuelve la misma posición original.
    """
    salto = tablero[posicion]
    if salto > 0:
        print(f"¡Escalera! Avanzás {salto} casillas.")
        res = posicion + salto
    else:
        res = posicion
    
    return res

def aplica_serpientes(posicion) -> int:
    """
    Función que verifica si la posición actual del jugador contiene una serpiente y,
    de ser así, aplica el retroceso correspondiente. En caso contrario, mantiene la
    misma posición.

    El tablero tiene marcadas las serpientes como valores positivos en las posiciones
    donde empiezan. Si hay una serpiente, el jugador retrocede la cantidad indicada.

    Args:
        posicion (int): Número de casilla donde se encuentra actualmente el jugador.

    Returns:
        int: Devuelve la nueva posición del jugador luego de aplicar la serpiente (si existe).
            Si no hay serpiente, devuelve la misma posición original.
    """
    salto = tablero[posicion]
    if salto > 0:
        print(f"¡Serpiente! Retrocedes {salto} casillas.")
        res = posicion - salto
    else:
        res = posicion
    
    return res
    
def turno(nombre, posicion, puntaje) -> any:
    """
    Función que representa el turno de un jugador. Durante el turno:
    - Muestra la posición actual del jugador
    - Realiza una pregunta
    - Si responde correctamente, avanza una casilla, suma un punto, y aplica escalera (si corresponde)
    - Si responde incorrectamente, retrocede una casilla, descuenta un punto, y aplica serpiente (si corresponde)
    - Devuelve la nueva posición y el puntaje actualizado

    Args:
        nombre (str): Nombre del jugador.
        posicion (int): Posición actual del jugador en el tablero.
        puntaje (int): Puntaje actual del jugador.

    Returns:
        tuple: Una tupla (nueva_posicion, nuevo_puntaje) con la actualización del turno.
    """
    print(f"\n{nombre}, estás en la casilla {posicion}")
    if pregunta():
        print("¡Correcto! Avanzas.")
        posicion += 1
        puntaje += 1
        posicion = aplica_escaleras(posicion)
        res = posicion, puntaje
    else:
        print("Incorrecto, retrocedes.")
        posicion -= 1
        puntaje -= 1
        posicion = aplica_serpientes(posicion)
        res = posicion, puntaje
    
    return res
    
def sigue_jugando() -> bool:
    """
    Función que consulta al jugador si desea seguir jugando.

    Muestra un mensaje por consola pidiendo confirmación, interpretando
    la respuesta 's' (minúscula) como continuar y cualquier otra opción
    como detener el juego.

    Returns:
        bool: True si el jugador quiere continuar (responde 's'),
            False en caso contrario.
    """
    seguir = input("¿Deseas continuar? (s/n): ").lower()
    res = seguir == 's'
    return res

def jugar(nombre:str, posicion:int, puntaje:int):
    """
    Función principal que controla el desarrollo completo de la partida para un jugador.

    Durante la partida:
    - Ejecuta turnos hasta que el jugador alcance la casilla 30 (gana), se quede sin preguntas disponibles, o decida abandonar.
    - En cada turno se actualiza la posición y el puntaje según respuestas correctas o incorrectas.
    - Registra el puntaje final al terminar la partida.
    - Informa el motivo de finalización: victoria, abandono o falta de preguntas.

    Args:
        nombre (str): Nombre del jugador.
        posicion (int): Posición inicial del jugador en el tablero.
        puntaje (int): Puntaje inicial del jugador.
    """

    flag_seguir = True
    flag_preguntas = True
    while posicion > 0 and posicion < 30 and flag_seguir and flag_preguntas:
        if len(preguntas) == 0:
            flag_preguntas = False
        else:
            posicion, puntaje = turno(nombre, posicion, puntaje)
            flag_seguir = sigue_jugando()

    if posicion == 30:
        print("GANADOR")
    elif flag_seguir == False:
        print("Se terminó el juego por abandono")
    elif flag_preguntas == False:
        print("Se terminó el juego por falta de preguntas")
    else:
        print("PERDEDOR")
    
    print(f"Su puntaje fue de {puntaje}")

    guarda_puntaje(nombre,posicion,puntaje)


nombre = input("Ingrese su nombre: ")
jugar(nombre,posicion,puntaje)



