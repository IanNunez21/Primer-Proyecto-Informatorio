import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Menú desplegable')
ventana.geometry('400x200')

# Crear la barra de menú y configurarla en la ventana
barra_menu = tk.Menu(ventana)
ventana.config(menu=barra_menu)

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
submenu.add_command(label='Opción 1', command=ventana.quit)
submenu.add_command(label='Opción 2', command=mostrar_mensaje)

# Iniciar el bucle principal de la ventana
ventana.mainloop()