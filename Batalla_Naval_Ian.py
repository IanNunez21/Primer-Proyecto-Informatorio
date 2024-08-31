import tkinter as tk
from PIL import Image, ImageTk
import pygame
import random

class Musica:
    def __init__(self, archivo_musica):
        pygame.mixer.init()
        self.reproducir_musica(archivo_musica)

    def reproducir_musica(self, archivo_musica):
        pygame.mixer.music.load(archivo_musica)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play(-1)

class VentanaBase:
    def __init__(self, titulo, ancho, alto, imagen_fondo, musica_fondo):
        self.ventana = tk.Tk()
        self.ventana.title(titulo)

        # Obtener el tamaño de la pantalla
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()

        # Calcular las coordenadas de la esquina superior izquierda para centrar la ventana
        x = (screen_width - ancho) // 2
        y = (screen_height - alto) // 2
        self.ventana.geometry(f'{400}x{200}+{x}+{y}')

        self.imagen_original = Image.open(imagen_fondo)

        self.label_fondo = tk.Label(self.ventana)
        self.label_fondo.place(x=0, y=0, relwidth=1, relheight=1)
        self.ventana.bind("<Configure>", self.actualizar_fondo)

    def actualizar_fondo(self, event):
        ancho = self.ventana.winfo_width()
        alto = self.ventana.winfo_height()

        imagen_redimensionada = self.imagen_original.resize((ancho, alto), Image.Resampling.LANCZOS)
        imagen_fondo = ImageTk.PhotoImage(imagen_redimensionada)

        self.label_fondo.config(image=imagen_fondo)
        self.label_fondo.image = imagen_fondo

class VentanaInicio(VentanaBase):
    def __init__(self, musica):
        super().__init__('Batalla Naval 🚢', 400, 200, "Fondo.png", musica)

        self.boton_abrir = tk.Button(self.ventana, text="Comenzar Juego", width=20, height=2, command=self.abrir_ventana)
        self.boton_abrir.pack(pady=10)

        self.boton_salir = tk.Button(self.ventana, text="Salir Juego", width=20, height=2, command=self.ventana.destroy)
        self.boton_salir.pack(pady=10)

        # Levantar los botones para que estén sobre la imagen de fondo
        self.boton_abrir.pack(pady=10, expand=True)
        self.boton_salir.pack(pady=10, expand=True)

    def abrir_ventana(self):
        self.ventana.destroy()
        ventana_dificultad = VentanaDificultad('Musica_Fondo.mp3')
        ventana_dificultad.ventana.mainloop()

class VentanaDificultad(VentanaBase):
    def __init__(self, musica):
        super().__init__('Selecciona Nivel de Dificultad', 400, 200, "Fondo.png", musica)

        self.boton_facil = tk.Button(self.ventana, text="Fácil", command=lambda: self.seleccionar_dificultad("Fácil"))
        self.boton_facil.pack(pady=10)

        self.boton_medio = tk.Button(self.ventana, text="Medio", command=lambda: self.seleccionar_dificultad("Medio"))
        self.boton_medio.pack(pady=10)

        self.boton_dificil = tk.Button(self.ventana, text="Difícil", command=lambda: self.seleccionar_dificultad("Difícil"))
        self.boton_dificil.pack(pady=10)

        self.boton_facil.pack(pady=10, expand=True)
        self.boton_medio.pack(pady=10, expand=True)
        self.boton_dificil.pack(pady=10, expand=True)

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
            self.boton_volver()
        else:
            if self.tablero[fila][columna] == "🌊":
                self.tablero[fila][columna] = "❌"
                self.intentos -= 1
                self.mostrar_tablero()
                self.resultado_label.config(text=f"Fallaste. Te quedan {self.intentos} intentos.", fg="red")

                if self.intentos == 0:
                    self.resultado_label.config(text=f"¡Juego terminado! El barco estaba en la posición: {self.barco}", fg="red")
                    self.deshabilitar_botones()
                    self.boton_volver()

    def deshabilitar_botones(self):
        for fila in range(9):
            for columna in range(9):
                self.botones[fila][columna].config(state="disabled")

    def boton_volver(self):
        boton_volver = tk.Button(self.ventana, text = 'Volver al menú', command=self.volver_al_menu)
        boton_volver.grid(row=10, column=0, columnspan=9)

    def volver_al_menu(self):
        self.ventana.destroy()
        juego = VentanaInicio() # Creo nueva instancia del juego

# Iniciar el juego
musica= Musica('Musica_Fondo.mp3')
juego = VentanaInicio(musica)
juego.ventana.mainloop()
