import tkinter as tk

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
# -------------------------------------------------------------------------------------------------------------
ventana2 = tk.Tk()
ventana2.title('Lista de tareas')
ventana2.geometry('400x200')

# Creamos un campo de texto para ingresar tareas
ingreso_tarea = tk.Entry(ventana2)
ingreso_tarea.pack()  # Empaquetamos el campo de texto en la ventana


# Definimos una funcion que nos permite agregar tareas a la lista
def agregar_tarea():
    tarea = ingreso_tarea.get()  # Obtenemos el texto ingresado en el campo de texto
    if tarea:  # Verificamos que el texto no este vacio
        lista_tareas.insert(tk.END, tarea)  # Agregamos la tarea a la lista
        ingreso_tarea.delete(0, tk.END)  # Limpiamos el campo de texto


# Creamos un boton para agregar tareas a la lista usando la funcion agregar_tarea
boton_agregar = tk.Button(ventana2, text='Agregar tarea', command=agregar_tarea)

# Ademas podemos agregar tareas al presionar enter en el campo de texto
# Al presionar enter se llama a la funcion agregar_tarea.
# Lambda es una funcion anonima que nos permite pasar argumentos a la funcion.
# <Return> es el evento que se dispara al presionar la tecla enter
# Bind (metodo) nos permite asociar un evento a un widget (en este caso el campo de texto)
ingreso_tarea.bind('<Return>', lambda event: agregar_tarea())


boton_agregar.pack()  # Empaquetamos el boton en la ventana


# Definimos una funcion que nos permite eliminar tareas de la lista
def eliminar_tarea():
    seleccion = lista_tareas.curselection()  # Obtenemos la tarea seleccionada
    if seleccion:  # Verificamos que se haya seleccionado una tarea
        lista_tareas.delete(seleccion)  # Eliminamos la tarea de la lista


boton_eliminar = tk.Button(
    ventana2, text='Eliminar tarea', command=eliminar_tarea)  # Creamos un boton para eliminar tareas de la lista usando la funcion eliminar_tarea
boton_eliminar.pack()  # Empaquetamos el boton en la ventana

lista_tareas = tk.Listbox(ventana2)  # Creamos una lista para mostrar las tareas
lista_tareas.pack()  # Empaquetamos la lista en la ventana

ventana2.mainloop()  # Iniciamos el bucle principal
