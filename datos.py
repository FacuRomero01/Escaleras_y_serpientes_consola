def guarda_puntaje(nombre: str, posicion: int, puntaje: int) -> None:
    """
    Guarda el puntaje del jugador en el archivo scores.csv.

    Cada línea del archivo almacena:
    - nombre del jugador
    - posición final alcanzada
    - puntaje final obtenido
    
    separados por comas, en formato CSV.

    Args:
        nombre (str): Nombre del jugador.
        posicion (int): Casillero en el que terminó el jugador.
        puntaje (int): Puntaje final del jugador.

    Returns:
        None: La función no devuelve nada, solo escribe en el archivo.
    """
    with open("scores.csv", "a") as archivo:
        archivo.write(f"{nombre},{posicion},{puntaje}\n")