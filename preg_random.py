
import random

def hacer_pregunta(preguntas) -> bool:
    
    preg_selec = random.choice(preguntas)

    print(f"\n{preg_selec['pregunta']}")
    opciones = {
        "a": preg_selec["respuesta_a"],
        "b": preg_selec["respuesta_b"],
        "c": preg_selec["respuesta_c"],
    }
    
    for letra, texto in opciones.items():
        print(f"{letra}. {texto}")

    flag_opcion = True
    while flag_opcion:
        respuesta = input(f"Elige una opción (a, b, c): ")
        if respuesta in opciones:
            res = respuesta == preg_selec["respuesta_correcta"]
            flag_opcion = False
        else:
            print("Opción inválida. Intenta de nuevo.")

    
    preguntas.remove(preg_selec)
    
    return res
    
    