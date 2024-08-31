import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random

class BatallaNaval:
    def __init__(self):
        pygame.mixer.init()
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title('Batalla Naval 🚢')
        self.ventana_principal.geometry('400x200')

        self.imagen_original = Image.open("Fondo.png")

        # Crear un label con la imagen de fondo
        self.label_fondo = tk.Label(self.ventana_principal)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana_principal.bind("<Configure>", self.actualizar_fondo)

        self.boton_abrir = tk.Button(self.ventana_principal, text="Comenzar Juego", command=self.abrir_ventana)
        self.boton_abrir.pack(pady=10)

        self.boton_salir = tk.Button(self.ventana_principal, text="Salir Juego", command=self.ventana_principal.destroy)
        self.boton_salir.pack(pady=10)

        # Crear la barra de menú
        self.barra_menu = tk.Menu(self.ventana_principal)
        self.ventana_principal.config(menu=self.barra_menu)

        self.menu_principal = tk.Menu(self.barra_menu, tearoff=0)
        self.barra_menu.add_cascade(label='Principal', menu=self.menu_principal)

        self.submenu = tk.Menu(self.menu_principal, tearoff=0)
        self.menu_principal.add_cascade(label='Opciones', menu=self.submenu)

        self.submenu.add_command(label='Opción 1', command=self.ventana_principal.destroy)
        self.submenu.add_command(label='Opción 2', command=self.mostrar_mensaje)

        # Reproducir la música de fondo
        self.reproducir_musica()

        # Levantar los botones para que estén sobre la imagen de fondo
        self.boton_abrir.lift()
        self.boton_salir.lift()

        # Iniciar el bucle principal de la ventana
        self.ventana_principal.mainloop()

    def reproducir_musica(self):
        pygame.mixer.music.load("Musica_Fondo.mp3")
        pygame.mixer.music.set_volume(0.4)
        pygame.mixer.music.play(-1)

    def actualizar_fondo(self, event):
        ancho = self.ventana_principal.winfo_width()
        alto = self.ventana_principal.winfo_height()

        imagen_redimensionada = self.imagen_original.resize((ancho, alto), Image.Resampling.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen_redimensionada)

        self.label_fondo.config(image=imagen_fondo)
        self.label_fondo.image = imagen_fondo

    def abrir_ventana(self):
        self.ventana_principal.destroy()

        ventana_dificultad = VentanaDificultad()
        ventana_dificultad.ventana.mainloop()

    def mostrar_mensaje(self):
        print('Mensaje')


class VentanaDificultad:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Selecciona Nivel de Dificultad')
        self.ventana.geometry('400x200')

        self.boton_facil = tk.Button(self.ventana, text="Fácil", command=lambda: self.seleccionar_dificultad("Fácil"))
        self.boton_facil.pack(pady=10)

        self.boton_medio = tk.Button(self.ventana, text="Medio", command=lambda: self.seleccionar_dificultad("Medio"))
        self.boton_medio.pack(pady=10)

        self.boton_dificil = tk.Button(self.ventana, text="Difícil", command=lambda: self.seleccionar_dificultad("Difícil"))
        self.boton_dificil.pack(pady=10)

    def seleccionar_dificultad(self, nivel):
        print(f"Nivel seleccionado: {nivel}")
        self.ventana.destroy()

        if nivel == "Difícil":
            juego_dificil = JuegoDificil()
            juego_dificil.ventana.mainloop()


class JuegoDificil:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Batalla Naval - Nivel Difícil 🚢')

        self.tablero = self.crear_tablero()
        self.barco = self.colocar_barco()
        self.intentos = 6

        self.botones = []
        for fila in range(9):
            fila_botones = []
            for columna in range(9):
                boton = tk.Button(self.ventana, text="🌊", width=4, height=2,
                                  command=lambda f=fila, c=columna: self.manejar_click(f, c))
                boton.grid(row=fila, column=columna)
                fila_botones.append(boton)
            self.botones.append(fila_botones)

        self.resultado_label = tk.Label(self.ventana, text=f"Tienes {self.intentos} intentos para hundir el barco.")
        self.resultado_label.grid(row=9, column=0, columnspan=9)

    def crear_tablero(self):
        return [["🌊"] * 9 for _ in range(9)]

    def colocar_barco(self):
        fila = random.randint(0, 8)
        columna = random.randint(0, 8)
        return fila, columna

    def mostrar_tablero(self):
        for fila in range(9):
            for columna in range(9):
                self.botones[fila][columna].config(text=self.tablero[fila][columna])

    def manejar_click(self, fila, columna):
        if (fila, columna) == self.barco:
            self.tablero[fila][columna] = "💥"
            self.mostrar_tablero()
            self.resultado_label.config(text="¡Hundiste el barco! 🚢", fg="green")
            self.deshabilitar_botones()
        else:
            if self.tablero[fila][columna] == "🌊":
                self.tablero[fila][columna] = "❌"
                self.intentos -= 1
                self.mostrar_tablero()
                self.resultado_label.config(text=f"Fallaste. Te quedan {self.intentos} intentos.", fg="red")

                if self.intentos == 0:
                    self.resultado_label.config(text=f"¡Juego terminado! El barco estaba en la posición: {self.barco}", fg="red")
                    self.deshabilitar_botones()

    def deshabilitar_botones(self):
        for fila in range(9):
            for columna in range(9):
                self.botones[fila][columna].config(state="disabled")


if __name__ == "__main__":
    juego = BatallaNaval()
