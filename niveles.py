import tkinter as tk
import random

# Diccionario para los niveles de dificultad
niveles_dificultad = {
    "Fácil": 6,  # Número de barcos en nivel fácil
    "Medio": 4,  # Número de barcos en nivel medio
    "Difícil": 2 # Número de barcos en nivel difícil
}

# Crear el tablero
def crear_tablero():
    return [["🌊"] * 9 for _ in range(9)]

# Mostrar el tablero en Tkinter
def mostrar_tablero(tablero, botones):
    for fila in range(9):
        for columna in range(9):
            botones[fila][columna].config(text=tablero[fila][columna])

# Colocar los barcos en posiciones aleatorias
def colocar_barcos(cantidad):
    barcos = set()
    while len(barcos) < cantidad:
        barco = (random.randint(0, 8), random.randint(0, 8))
        barcos.add(barco)
    return barcos

# Función para manejar el clic en un botón
def manejar_click(fila, columna):
    global intentos, barcos, tablero, botones

    if (fila, columna) in barcos:
        tablero[fila][columna] = "💥"
        barcos.remove((fila, columna))
        mostrar_tablero(tablero, botones)
        if not barcos:
            resultado_label.config(text="¡Hundiste todos los barcos! 🚢", fg="green")
            for f in range(9):
                for c in range(9):
                    botones[f][c].config(state="disabled")
    else:
        if tablero[fila][columna] == "🌊":
            tablero[fila][columna] = "❌"
            intentos -= 1
            mostrar_tablero(tablero, botones)
            resultado_label.config(text=f"Fallaste. Te quedan {intentos} intentos.", fg="red")

            if intentos == 0:
                resultado_label.config(text=f"¡Juego terminado! Los barcos estaban en las posiciones: {barcos}", fg="red")
                for f in range(9):
                    for c in range(9):
                        botones[f][c].config(state="disabled")

# Función para iniciar el juego con el nivel seleccionado
def iniciar_juego(nivel):
    global intentos, barcos, tablero, botones, resultado_label

    # Configuración inicial del juego
    ventana_juego = tk.Tk()
    ventana_juego.title(f'Batalla Naval - Nivel {nivel} 🚢')

    tablero = crear_tablero()
    barcos = colocar_barcos(niveles_dificultad[nivel])
    intentos = niveles_dificultad[nivel] * 2  # Número de intentos basado en la cantidad de barcos

    # Crear botones para la cuadrícula
    botones = []
    for fila in range(9):
        fila_botones = []
        for columna in range(9):
            boton = tk.Button(ventana_juego, text="🌊", width=4, height=2, command=lambda f=fila, c=columna: manejar_click(f, c))
            boton.grid(row=fila, column=columna)
            fila_botones.append(boton)
        botones.append(fila_botones)

    # Etiqueta para mostrar el resultado
    resultado_label = tk.Label(ventana_juego, text=f"Tienes {intentos} intentos para hundir los barcos.")
    resultado_label.grid(row=9, column=0, columnspan=9)

    # Iniciar el bucle principal de la ventana
    ventana_juego.mainloop()

# Función para abrir la ventana de selección de nivel de dificultad
def abrir_ventana():
    ventana2.destroy()  # Cierra la ventana principal
    
    # Crear la nueva ventana para la selección de dificultad
    ventana1 = tk.Tk()
    ventana1.title('Selecciona Nivel de Dificultad')
    ventana1.geometry('400x200')

    # Función para manejar la selección de nivel de dificultad
    def seleccionar_dificultad(nivel):
        ventana1.destroy()  # Cerrar la ventana después de seleccionar
        iniciar_juego(nivel)

    # Crear botones de selección de nivel de dificultad
    boton_facil = tk.Button(ventana1, text="Fácil", command=lambda: seleccionar_dificultad("Fácil"))
    boton_facil.pack(pady=10)

    boton_medio = tk.Button(ventana1, text="Medio", command=lambda: seleccionar_dificultad("Medio"))
    boton_medio.pack(pady=10)

    boton_dificil = tk.Button(ventana1, text="Difícil", command=lambda: seleccionar_dificultad("Difícil"))
    boton_dificil.pack(pady=10)

    # Iniciar el bucle principal de la ventana
    ventana1.mainloop()

# Crear la ventana principal
ventana2 = tk.Tk()
ventana2.title('Batalla Naval🚢')
ventana2.geometry('400x200')

# Crear la barra de menú y configurarla en la ventana
barra_menu = tk.Menu(ventana2)
ventana2.config(menu=barra_menu)

# Crear el menú principal y agregarlo a la barra de menú
menu_principal = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label='Principal', menu=menu_principal)

# Crear un submenú y agregarlo al menú principal
submenu = tk.Menu(menu_principal, tearoff=0)
menu_principal.add_cascade(label='Opciones', menu=submenu)

# Definir una función para mostrar un mensaje
def mostrar_mensaje():
    print('Mensaje')

# Agregar opciones al submenú
submenu.add_command(label='Opción 1', command=ventana2.destroy)
submenu.add_command(label='Opción 2', command=mostrar_mensaje)

# Crear un botón en la ventana principal que abre la segunda ventana
boton_abrir = tk.Button(ventana2, text="Comenzar Juego", command=abrir_ventana)
boton_abrir.pack(pady=10)

# Crear un botón que cierra la aplicación
boton_salir = tk.Button(ventana2, text="Salir Juego", command=ventana2.destroy)
boton_salir.pack(pady=10)

# Iniciar el bucle principal de la ventana principal
ventana2.mainloop()
