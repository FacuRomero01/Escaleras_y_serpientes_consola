from datos import guarda_puntaje
from preg_random import hacer_pregunta
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
    salto = tablero[posicion]
    if salto > 0:
        print(f"¡Escalera! Avanzás {salto} casillas.")
        res = posicion + salto
    else:
        res = posicion
    
    return res

def aplica_serpientes(posicion) -> int:
    salto = tablero[posicion]
    if salto > 0:
        print(f"¡Serpiente! Retrocedes {salto} casillas.")
        res = posicion - salto
    else:
        res = posicion
    
    return res
    
def jugar(nombre, posicion, puntaje) -> any:
    
    flag_seguir = True
    flag_preguntas = True
    while posicion > 0 and posicion < 30 and flag_seguir and flag_preguntas:
        
        if len(preguntas) == 0:
            flag_preguntas = False
            break

        print(f"\n{nombre}, estás en la casilla {posicion}")

        if hacer_pregunta(preguntas):
            print("¡Correcto! Avanzas.")
            posicion += 1
            puntaje += 1
            posicion = aplica_escaleras(posicion)
        else:
            print("Incorrecto, retrocedes.")
            posicion -= 1
            puntaje -= 1
            posicion = aplica_serpientes(posicion)
        
        seguir = input("¿Deseas continuar? (s/n): ").lower()
        if seguir != 's':
            flag_seguir = False
    
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


