import random
import tkinter as tk
from colorama import Fore, init

init(autoreset=True)

# Tablero de juego
def crear_tablero():
    return [["🌊"] * 8 for _ in range(8)]

def mostrar_tablero(tablero):
    tablero_str = "\n".join([" ".join(fila) for fila in tablero])
    return tablero_str

# Colocar el barco en una posición aleatoria
def colocar_barco():
    fila = random.randint(0, 7)
    columna = random.randint(0, 7)
    return (fila, columna)

# Juego principal
def jugar(tablero_label, resultado_label, ventana):
    tablero = crear_tablero()
    barco = colocar_barco()
    intentos = 6  
    intentos_previos = []  # Guardar los intentos previos para evitar repeticiones

    resultado_label.config(text="Tienes 6 intentos para hundir el barco.")
    tablero_label.config(text=mostrar_tablero(tablero))

    def pedir_posicion():
        try:
            fila = int(entry_fila.get()) - 1  # Convertir a índice 0-7
            columna = int(entry_columna.get()) - 1  # Convertir a índice 0-7
            if 0 <= fila <= 7 and 0 <= columna <= 7:
                if (fila, columna) in intentos_previos:
                    resultado_label.config(text="Ya intentaste esa posición. Prueba en otra.")
                    return
                intentos_previos.append((fila, columna))  # Guardar el intento

                if (fila, columna) == barco:
                    tablero[fila][columna] = "💥"
                    tablero_label.config(text=mostrar_tablero(tablero))
                    resultado_label.config(text="¡Hundiste el barco!")
                    reiniciar_juego(ventana)
                else:
                    tablero[fila][columna] = "❌"
                    nonlocal intentos
                    intentos -= 1
                    tablero_label.config(text=mostrar_tablero(tablero))
                    resultado_label.config(text=f"Fallaste. Te quedan {intentos} intentos.")
                    if intentos == 0:
                        resultado_label.config(text=f"¡Juego terminado! El barco estaba en {barco}")
                        reiniciar_juego(ventana)
            else:
                resultado_label.config(text="Por favor, ingresa números dentro del rango (1-8).")
        except ValueError:
            resultado_label.config(text="Entrada inválida. Por favor, ingresa un número.")

    def reiniciar_juego(ventana):
        boton_reintentar = tk.Button(ventana, text="Volver a intentarlo", command=lambda: jugar(tablero_label, resultado_label, ventana))
        boton_reintentar.pack(pady=10)

    # Configuración de la interfaz
    entry_fila = tk.Entry(ventana)
    entry_fila.pack(pady=5)
    entry_fila.insert(0, "Fila (1-8)")

    entry_columna = tk.Entry(ventana)
    entry_columna.pack(pady=5)
    entry_columna.insert(0, "Columna (1-8)")

    boton_disparar = tk.Button(ventana, text="Disparar", command=pedir_posicion)
    boton_disparar.pack(pady=10)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Batalla Naval 🚢')

tablero_label = tk.Label(ventana, text="", font=("Courier", 12))
tablero_label.pack(pady=10)

resultado_label = tk.Label(ventana, text="", font=("Courier", 12), fg="blue")
resultado_label.pack(pady=10)

jugar(tablero_label, resultado_label, ventana)

ventana.mainloop()
