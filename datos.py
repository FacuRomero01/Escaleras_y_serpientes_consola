
def guarda_puntaje(nombre, posicion, puntaje):
    with open("scores.csv", "a") as archivo:
        archivo.write(f"{nombre},{posicion},{puntaje}\n")

