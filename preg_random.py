import random
from preguntas import preguntas

def selecciona_pregunta(preguntas: list) -> dict:
    """
    Selecciona aleatoriamente una pregunta de la lista de preguntas disponibles.

    Args:
        preguntas (list): Lista de diccionarios, cada uno representando una pregunta con sus opciones.

    Returns:
        dict: Diccionario que representa la pregunta seleccionada aleatoriamente.
    """
    preg_selec = random.choice(preguntas)
    return preg_selec

def muestra_pregunta(pregunta: dict):
    """
    Muestra en consola la pregunta y sus posibles respuestas.

    Args:
        pregunta (dict): Diccionario que contiene el texto de la pregunta y las tres opciones (respuesta_a, respuesta_b, respuesta_c).
    """
    print(f"\n{pregunta['pregunta']}")
    print(f"a. {pregunta['respuesta_a']}")
    print(f"b. {pregunta['respuesta_b']}")
    print(f"c. {pregunta['respuesta_c']}")

def ingresa_opcion() -> str:
    """
    Solicita al usuario que ingrese una opción de respuesta.

    Returns:
        str: Letra elegida por el usuario ("a", "b" o "c").
    """
    respuesta = input("Elige una opción (a, b, c): ")
    return respuesta

def valida_respuesta(pregunta: dict) -> bool:
    """
    Valida si la opción ingresada por el usuario coincide con la respuesta correcta
    de la pregunta.

    Solicita repetidamente la opción al usuario hasta que ingrese una opción válida
    (a, b o c). Luego compara la opción elegida con la respuesta correcta definida
    en el diccionario de la pregunta.

    Args:
        pregunta (dict): Diccionario que contiene la pregunta, opciones y la respuesta correcta.

    Returns:
        bool: True si la opción ingresada coincide con la correcta, False en caso contrario.
    """
    flag_opcion = True
    while flag_opcion:
        respuesta = ingresa_opcion()
        if respuesta in ["a", "b", "c"]:
            res = respuesta == pregunta["respuesta_correcta"]
            flag_opcion = False
        else:
            print("Opción inválida. Intenta de nuevo.")
    return res

def pregunta() -> bool:
    """
    Gestiona el ciclo completo de preguntar al usuario:

    - Selecciona aleatoriamente una pregunta de la lista de preguntas disponibles.
    - La muestra en consola con sus opciones.
    - Valida la respuesta ingresada.
    - Elimina la pregunta de la lista para no repetirla.

    Returns:
        bool: True si el usuario respondió correctamente, False si se equivocó.
    """
    preg_selec = selecciona_pregunta(preguntas)
    muestra_pregunta(preg_selec)
    res = valida_respuesta(preg_selec)
    preguntas.remove(preg_selec)
    return res