import tkinter as tk

# Función para abrir la segunda ventana
def abrir_ventana():
    # Cierra la ventana principal
    ventana2.destroy()
    
    ventana1 = tk.Tk()
    ventana1.title('Barra de desplazamiento')
    ventana1.geometry('400x200')

    marco = tk.Frame(ventana1)  # frame es un contenedor
    # posiciona el frame en la ventana con un padding de 10 en x y en y
    marco.pack(padx=10, pady=10)

    scrollbar = tk.Scrollbar(marco)  # crea un scrollbar en el frame
    # posiciona el scrollbar en el frame a la derecha y que se expanda en y
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    lista = tk.Listbox(marco, yscrollcommand=scrollbar.set) # crea una lista en el frame
    for i in range(100): # agrega 100 elementos a la lista
        lista.insert(tk.END, f'Elemento {i+1}') # inserta un elemento al final de la lista

    lista.pack(side=tk.LEFT, fill=tk.BOTH) # posiciona la lista a la izquierda y que se expanda en x y en y

    scrollbar.config(command=lista.yview) # configura el scrollbar para que controle la vista en y de la lista

    ventana1.mainloop() # inicia el bucle principal de la ventana

# Crear la ventana principal
ventana2 = tk.Tk()
ventana2.title('Batalla Naval🚢')
ventana2.geometry('400x200')

# Crear la barra de menú y configurarla en la ventana
barra_menu = tk.Menu(ventana2)
ventana2.config(menu=barra_menu)

# Crear el menú principal y agregarlo a la barra de menú
menu_principal = tk.Menu(barra_menu, tearoff=0)  # tearoff=0 para evitar el separador, lo que hace el tearoff aqui es que se pueda separar el menu principal de la barra de menu
barra_menu.add_cascade(label='Principal', menu=menu_principal)

# Crear un submenú y agregarlo al menú principal
submenu = tk.Menu(menu_principal, tearoff=0)  # tearoff=0 para evitar el separador, lo que hace el tearoff es que se pueda separar el submenu del menu principal
menu_principal.add_cascade(label='Opciones', menu=submenu)

# Definir una función para mostrar un mensaje
def mostrar_mensaje():
    print('Mensaje')

# Agregar opciones al submenú
submenu.add_command(label='Opción 1', command=ventana2.quit)
submenu.add_command(label='Opción 2', command=mostrar_mensaje)

# Crear un botón en la ventana principal que abre la segunda ventana
boton_abrir = tk.Button(ventana2, text="Comenzar Juego", command=abrir_ventana)
boton_abrir.pack(pady=10)

# Iniciar el bucle principal de la ventana
ventana2.mainloop()
ventana2.mainloop()  # Iniciamos el bucle principal
