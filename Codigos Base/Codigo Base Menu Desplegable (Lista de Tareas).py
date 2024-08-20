import tkinter as tk

ventana = tk.Tk()
ventana.title('Lista de tareas')
ventana.geometry('400x200')

# Creamos un campo de texto para ingresar tareas
ingreso_tarea = tk.Entry(ventana)
ingreso_tarea.pack()  # Empaquetamos el campo de texto en la ventana


# Definimos una funcion que nos permite agregar tareas a la lista
def agregar_tarea():
    tarea = ingreso_tarea.get()  # Obtenemos el texto ingresado en el campo de texto
    if tarea:  # Verificamos que el texto no este vacio
        lista_tareas.insert(tk.END, tarea)  # Agregamos la tarea a la lista
        ingreso_tarea.delete(0, tk.END)  # Limpiamos el campo de texto


# Creamos un boton para agregar tareas a la lista usando la funcion agregar_tarea
boton_agregar = tk.Button(ventana, text='Agregar tarea', command=agregar_tarea)

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
    ventana, text='Eliminar tarea', command=eliminar_tarea)  # Creamos un boton para eliminar tareas de la lista usando la funcion eliminar_tarea
boton_eliminar.pack()  # Empaquetamos el boton en la ventana

lista_tareas = tk.Listbox(ventana)  # Creamos una lista para mostrar las tareas
lista_tareas.pack()  # Empaquetamos la lista en la ventana

ventana.mainloop()  # Iniciamos el bucle principal