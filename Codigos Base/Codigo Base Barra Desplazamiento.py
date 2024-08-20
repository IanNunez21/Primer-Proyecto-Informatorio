import tkinter as tk

ventana = tk.Tk()
ventana.title('Barra de desplazamiento')
ventana.geometry('400x200')

marco = tk.Frame(ventana)  # frame es un contenedor
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

ventana.mainloop() # inicia el bucle principal de la ventana