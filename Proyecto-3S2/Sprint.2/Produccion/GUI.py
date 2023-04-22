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

class Ventana3:
    def __init__(self, master, filas, columnas):
        self.master = master
        self.master.title("Tablero")

        # Crea un frame para la izquierda de la ventana
        self.frame_izquierdo = tk.Frame(self.master, padx=10, pady=10)
        self.frame_izquierdo.pack(side="left", fill="y")

        # Crea el título "Blue Player"
        self.titulo_blue = tk.Label(self.frame_izquierdo, text="Blue Player", font=("Arial", 16))
        self.titulo_blue.pack(pady=10)

        # Crea los radio buttons para elegir entre S y O
        self.blue_var = tk.StringVar()
        self.blue_var.set("S")
        self.blue_radio_s = tk.Radiobutton(self.frame_izquierdo, text="S", variable=self.blue_var, value="S")
        self.blue_radio_s.pack()
        self.blue_radio_o = tk.Radiobutton(self.frame_izquierdo, text="O", variable=self.blue_var, value="O")
        self.blue_radio_o.pack()

        # Crea un frame para el tablero
        self.frame_tablero = tk.Frame(self.master, padx=10, pady=10)
        self.frame_tablero.pack(side="left")

        # Crea las casillas del tablero
        self.casillas = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                casilla = tk.Label(self.frame_tablero, text="", font=("Arial", 32), width=4, height=2, relief="solid", borderwidth=2)
                casilla.grid(row=i, column=j)
                fila.append(casilla)
            self.casillas.append(fila)

        # Crea un frame para la derecha de la ventana
        self.frame_derecho = tk.Frame(self.master, padx=10, pady=10)
        self.frame_derecho.pack(side="right", fill="y")

        # Crea el título "Red Player"
        self.titulo_red = tk.Label(self.frame_derecho, text="Red Player", font=("Arial", 16))
        self.titulo_red.pack(pady=10)

        # Crea los radio buttons para elegir entre S y O
        self.red_var = tk.StringVar()
        self.red_var.set("S")
        self.red_radio_s = tk.Radiobutton(self.frame_derecho, text="S", variable=self.red_var, value="S")
        self.red_radio_s.pack()
        self.red_radio_o = tk.Radiobutton(self.frame_derecho, text="O", variable=self.red_var, value="O")
        self.red_radio_o.pack()

        # Añade el botón para volver a la ventana anterior
        self.boton_volver = tk.Button(self.frame_izquierdo, text="Volver", font=("Arial", 16), command=self.volver)
        self.boton_volver.pack(side="bottom", pady=10, anchor="sw")

        # Añade el botón para iniciar el juego
        self.boton_iniciar = tk.Button(self.frame_derecho, text="Iniciar Juego", font=("Arial", 16), command=self.iniciar_juego)
        self.boton_iniciar.pack(side="bottom", pady=10, anchor="s")


    def volver(self):
        # Cierra la ventana actual
        self.master.destroy()

        # Muestra la ventana anterior
        self.master.master.deiconify()

    def iniciar_juego(self):
        # TODO: Lógica para iniciar el juego
        pass

# Crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.geometry("400x400")

# Muestra la primera ventana
ventana1 = Ventana1(ventana_principal)

# Mantiene la ventana principal en bucle
ventana_principal.mainloop()
