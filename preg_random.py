import random
from preguntas import preguntas

def selecciona_pregunta(preguntas:list) -> dict:
    preg_selec = random.choice(preguntas)
    return preg_selec


def muestra_pregunta(pregunta:dict) -> list:
    print(f"\n{pregunta["pregunta"]}")
    print(f"a. {pregunta["respuesta_a"]}")
    print(f"b. {pregunta["respuesta_b"]}")
    print(f"c. {pregunta["respuesta_c"]}")


def ingresa_opcion()-> chr:
    respuesta = input(f"Elige una opción (a, b, c): ")
    return respuesta

def valida_respuesta(pregunta:dict) -> any:
    flag_opcion = True
    while flag_opcion:
        respuesta = ingresa_opcion()
        if respuesta == "a" or respuesta == "b" or respuesta == "c":
            res = respuesta == pregunta["respuesta_correcta"]
            flag_opcion = False
        else:
            print("Opción inválida. Intenta de nuevo.")
    return res

def pregunta() -> bool:
    preg_selec = selecciona_pregunta(preguntas)
    muestra_pregunta(preg_selec)
    res = valida_respuesta(preg_selec)
    preguntas.remove(preg_selec)
    return res