import random
from colorama import Fore, Style, init

# Inicializar colorama
init(autoreset=True)

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
            fila = int(input(Fore.CYAN+"Ingresa el número de fila (0-8): "))
            columna = int(input(Fore.CYAN+"Ingresa el número de columna (0-8): "))
            if 0 <= fila <= 8 and 0 <= columna <= 8:
                return (fila, columna)
            else:
                print(Fore.RED+"Por favor, ingresa números dentro del rango (0-8).")
        except ValueError:
            print(Fore.RED+"Entrada inválida. Por favor, ingresa un número.")

# Juego principal
def jugar():
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 6  

    print(Fore.CYAN + " _ ____  _                           _     _                 ____        _        _ _         _   _                  _ _ ")
    print(Fore.CYAN + "(_) __ )(_) ___ _ ____   _____ _ __ (_) __| | ___     __ _  | __ )  __ _| |_ __ _| | | __ _  | \\ | | __ ___   ____ _| | |")
    print(Fore.CYAN + "| |  _ \\| |/ _ \\ '_ \\ \\ / / _ \\ '_ \\| |/ _` |/ _ \\   / _` | |  _ \\ / _` | __/ _` | | |/ _` | |  \\| |/ _` \\ \\ / / _` | | |")
    print(Fore.CYAN + "| | |_) | |  __/ | | \\ V /  __/ | | | | (_| | (_) | | (_| | | |_) | (_| | || (_| | | | (_| | | |\\  | (_| |\\ V / (_| | |_|")
    print(Fore.CYAN + "|_|____/|_|\\___|_| |_|\\_/ \\___|_| |_|_|\\__,_|\\___/   \\__,_| |____/ \\__,_|\\__\\__,_|_|_|\\__,_| |_| \\_|\\__,_| \\_/ \\__,_|_(_)")
    print(Fore.YELLOW + "Tienes 6 intentos para hundir el barco 🚢.")
    mostrar_tablero(tablero)

    while intentos > 0:
        fila, columna = pedir_posicion()

        if (fila, columna) == barco:
            print(Fore.GREEN + "███████╗███████╗██╗     ██╗ ██████╗██╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗")
            print(Fore.GREEN + "██╔════╝██╔════╝██║     ██║██╔════╝██║██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔════╝██║")
            print(Fore.GREEN + "█████╗  █████╗  ██║     ██║██║     ██║██║  ██║███████║██║  ██║█████╗  ███████╗██║")
            print(Fore.GREEN + "██╔══╝  ██╔══╝  ██║     ██║██║     ██║██║  ██║██╔══██║██║  ██║██╔══╝  ╚════██║╚═╝")
            print(Fore.GREEN + "██║     ███████╗███████╗██║╚██████╗██║██████╔╝██║  ██║██████╔╝███████╗███████║██╗")
            print(Fore.GREEN + "╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝╚═╝╚═════╝ ╚═╝  ╚═╝╚═════╝ ╚══════╝╚══════╝╚═╝")
            print(Fore.GREEN + "Hundiste el barco 🚢")

            tablero[fila][columna] = "💥"
            mostrar_tablero(tablero)
            break
        else:
            print(Fore.RED + "███████╗░█████╗░██╗░░░░░██╗░░░░░░█████╗░░██████╗████████╗███████╗██╗")
            print(Fore.RED + "██╔════╝██╔══██╗██║░░░░░██║░░░░░██╔══██╗██╔════╝╚══██╔══╝██╔════╝██║")
            print(Fore.RED + "█████╗░░███████║██║░░░░░██║░░░░░███████║╚█████╗░░░░██║░░░█████╗░░██║")
            print(Fore.RED + "██╔══╝░░██╔══██║██║░░░░░██║░░░░░██╔══██║░╚═══██╗░░░██║░░░██╔══╝░░╚═╝")
            print(Fore.RED + "██║░░░░░██║░░██║███████╗███████╗██║░░██║██████╔╝░░░██║░░░███████╗██╗")
            print(Fore.RED + "╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚══════╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚══════╝╚═╝")
        tablero[fila][columna] = "❌"
        intentos -= 1
        print(Fore.YELLOW + f"Te quedan {intentos} intentos.")
        mostrar_tablero(tablero)

        if intentos == 0:
            print(Fore.RED + "¡Juego terminado! Se te acabaron los intentos.")
            print(Fore.RED + f"El barco estaba en la posición: {barco} 🚢")
            print(Fore.LIGHTMAGENTA_EX +"───│─────────────────────────────────────")
            print(Fore.LIGHTMAGENTA_EX +"───│────────▄▄───▄▄───▄▄───▄▄───────│────")
            print(Fore.LIGHTMAGENTA_EX +"───▌────────▒▒───▒▒───▒▒───▒▒───────▌────")
            print(Fore.LIGHTMAGENTA_EX +"───▌──────▄▀█▀█▀█▀█▀█▀█▀█▀█▀█▀▄─────▌────")
            print(Fore.LIGHTMAGENTA_EX +"───▌────▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄───▋────")
            print(Fore.LIGHTMAGENTA_EX +"▀██████████████████████████████████████▄─")
            print(Fore.LIGHTMAGENTA_EX +"──▀███████████████████████████████████▀──")
            print(Fore.LIGHTMAGENTA_EX +"─────▀██████████████████████████████▀────")
            print(Fore.LIGHTMAGENTA_EX +"▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            print(Fore.LIGHTMAGENTA_EX +"▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")
            print(Fore.LIGHTMAGENTA_EX +"▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒")

# Iniciar el juego
if __name__ == "__main__":
    jugar()
