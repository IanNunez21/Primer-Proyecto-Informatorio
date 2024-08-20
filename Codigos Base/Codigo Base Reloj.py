import tkinter as tk
import time

ventana = tk.Tk()  # crea la ventana
ventana.title('Reloj simple')  # Definimos el titulo de la ventana
ventana.geometry('400x200')  # Definimos el tamaÃ±o de la ventana
# Creamos un label para mostrar la hora
reloj = tk.Label(ventana, font=('Arial', 60), bg='black', fg='white')


# Definimos una funcion que nos permite obtener la hora actual
def hora():
    # utilizamos el modulo time y su metodo strftime para obtener la hora actual en formato HH:MM:SS
    tiempo_actual = time.strftime('%H:%M:%S')
    # Actualizamos el texto del label con la hora actual
    reloj.config(text=tiempo_actual)
    # Llamamos a la funcion hora cada 1000 milisegundos (1 segundo)
    ventana.after(1000, hora)


reloj.pack()  # Empaquetamos el label en la ventana
hora()  # Llamamos a la funcion hora para que se ejecute

ventana.mainloop()  # Iniciamos el bucle principal