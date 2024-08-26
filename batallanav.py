import tkinter as tk

# Función para abrir la segunda ventana con selección de nivel de dificultad
def abrir_ventana():
    ventana2.destroy()  # Cierra la ventana principal
    
    # Crear la nueva ventana para la selección de dificultad
    ventana1 = tk.Tk()
    ventana1.title('Selecciona Nivel de Dificultad')
    ventana1.geometry('400x200')

    # Función para manejar la selección de nivel de dificultad
    def seleccionar_dificultad(nivel):
        print(f"Nivel seleccionado: {nivel}")
        ventana1.destroy()  # Cerrar la ventana después de seleccionar

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
