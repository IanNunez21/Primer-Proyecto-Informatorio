import random

# tablero 
def crear_tablero():
    return [["🌊"] * 9 for _ in range(9)]

def mostrar_tablero(tablero):
    for fila in tablero:
        print(" ".join(fila))

# posición aleatoria barco
def colocar_barco():
    fila = random.randint(0, 8)
    columna = random.randint(0, 8)
    return (fila, columna)

# pedir una posición aleatoria
def pedir_posicion():
    while True:
        try:
            fila = int(input("Ingresa el número de fila (0-8): "))
            columna = int(input("Ingresa el número de columna (0-8): "))
            if 0 <= fila <= 8 and 0 <= columna <= 8:
                return (fila, columna)
            else:
                print("Por favor, ingresa números dentro del rango (0-8).")
        except ValueError:
            print("Entrada inválida. Por favor, ingresa un número.")

# Juego principal
def jugar():
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 6  

    print(" _ ____  _                           _     _                 ____        _        _ _         _   _                  _ _ ")
    print("(_) __ )(_) ___ _ ____   _____ _ __ (_) __| | ___     __ _  | __ )  __ _| |_ __ _| | | __ _  | \\ | | __ ___   ____ _| | |")
    print("| |  _ \\| |/ _ \\ '_ \\ \\ / / _ \\ '_ \\| |/ _` |/ _ \\   / _` | |  _ \\ / _` | __/ _` | | |/ _` | |  \\| |/ _` \\ \\ / / _` | | |")
    print("| | |_) | |  __/ | | \\ V /  __/ | | | | (_| | (_) | | (_| | | |_) | (_| | || (_| | | | (_| | | |\\  | (_| |\\ V / (_| | |_|")
    print("|_|____/|_|\\___|_| |_|\\_/ \\___|_| |_|_|\\__,_|\\___/   \\__,_| |____/ \\__,_|\\__\\__,_|_|_|\\__,_| |_| \\_|\\__,_| \\_/ \\__,_|_(_)")
    print("Tienes 6 intentos para hundir el barco 🚢.")
    mostrar_tablero(tablero)

    while intentos > 0:
        fila, columna = pedir_posicion()

        if (fila, columna) == barco:
            print("███████╗███████╗██╗     ██╗ ██████╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗")
            print("██╔════╝██╔════╝██║     ██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██║")
            print("█████╗  █████╗  ██║     ██║██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗██║")
            print("██╔══╝  ██╔══╝  ██║     ██║██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║╚═╝")
            print("██║     ███████╗███████╗██║╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║██╗")
            print("╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝")
            print("Hundiste el barco 🚢")
            
            tablero[fila][columna] = "💥"
            mostrar_tablero(tablero)
            break
        else:
            print("███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██████╗████████╗███████╗██╗")
            print("██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║")
            print("█████╗░░███████║██║░░░░░██║░░░░░███████║╚█████╗░░░░██║░░░█████╗░░██║")
            print("██╔══╝░░██╔══██║██║░░░░░██║░░░░░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░╚═╝")
            print("██║░░░░░██║░░██║███████╗███████╗██║░░██║██████╔╝░░░██║░░░███████╗██╗")
            print("╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝")
        tablero[fila][columna] = "❌"
        intentos -= 1
        print(f"Te quedan {intentos} intentos.")
        mostrar_tablero(tablero)

        if intentos == 0:
            print("¡Juego terminado! Se te acabaron los intentos.")
            print(f"El barco estaba en la posición: {barco} 🚢")

# Iniciar el juego
if __name__ == "__main__":
    jugar()
