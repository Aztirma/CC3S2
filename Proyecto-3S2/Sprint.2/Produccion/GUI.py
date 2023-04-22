import tkinter as tk

class Ventana1:
    def __init__(self, master):
        self.master = master
        self.master.title("S O S")

        # Añade widgets a la ventana
        self.etiqueta = tk.Label(self.master, text="Bienvenido a S O S", font=("Arial", 20))
        self.etiqueta.pack(pady=20)
        self.boton_singleplayer = tk.Button(self.master, text="Single Player", font=("Arial", 16),
                                            command=self.singleplayer)
        self.boton_singleplayer.pack(pady=10)
        self.boton_multiplayer = tk.Button(self.master, text="Multiplayer", font=("Arial", 16),
                                           command=self.multiplayer)
        self.boton_multiplayer.pack(pady=10)
        self.boton_salir = tk.Button(self.master, text="Salir", font=("Arial", 16), command=self.salir)
        self.boton_salir.pack(pady=10)

    def singleplayer(self):
            # Oculta la ventana principal
            self.master.withdraw()

    def multiplayer(self):
        # Oculta la ventana principal
        self.master.withdraw()

        # Crea la segunda ventana utilizando Toplevel
        ventana2 = tk.Toplevel()
        Ventana2(ventana2, self.master, "Multiplayer")

    def salir(self):
        # Cierra la ventana principal
        self.master.destroy()

class Ventana2:
    def __init__(self, master, ventana_principal, modo_juego):
        self.master = master
        self.master.title(modo_juego)
        self.ventana_principal = ventana_principal

        # Añade widgets a la ventana
        self.etiqueta = tk.Label(self.master, text=f"Modo de juego: {modo_juego}", font=("Arial", 20))
        self.etiqueta.pack(pady=20)

        # Añade el label y el entry para el tamaño de filas y columnas
        self.frame_tamaño = tk.Frame(self.master)
        self.frame_tamaño.pack(pady=10)
        self.label_tamaño = tk.Label(self.frame_tamaño, text="Tamaño del tablero:", font=("Arial", 16))
        self.label_tamaño.pack(side=tk.LEFT)
        self.entry_tamaño = tk.Entry(self.frame_tamaño, font=("Arial", 16), width=5)
        self.entry_tamaño.pack(side=tk.LEFT)

        # Añade el botón para comenzar el juego
        self.boton_comenzar = tk.Button(self.master, text="Comenzar", font=("Arial", 16), command=self.comenzar)
        self.boton_comenzar.pack(pady=10)

        # Añade el botón para volver a la ventana anterior
        self.boton_volver = tk.Button(self.master, text="Volver", font=("Arial", 16), command=self.volver)
        self.boton_volver.pack(pady=10)

    def comenzar(self):
        # Obtiene el tamaño del tablero ingresado por el usuario
        tamaño = int(self.entry_tamaño.get())

        # Cierra la ventana actual
        self.master.destroy()

        # Crea la Ventana3 y la muestra
        ventana3 = tk.Toplevel(self.ventana_principal)
        ventana3_gui = Ventana3(ventana3, tamaño, tamaño)

    def volver(self):
        # Cierra la ventana
        self.master.destroy()

        # Muestra la ventana principal
        self.ventana_principal.deiconify()

# Crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.geometry("400x400")

# Muestra la primera ventana
ventana1 = Ventana1(ventana_principal)

# Mantiene la ventana principal en bucle
ventana_principal.mainloop()
