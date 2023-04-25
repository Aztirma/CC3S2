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

    def __init__(self, master, ventana_principal, gamemod_2):
        self.master = master
        self.master.title(gamemod_2)
        self.ventana_principal = ventana_principal

        # Añade widgets a la ventana
        self.etiqueta = tk.Label(self.master, text=f"Modo de juego: {gamemod_2}", font=("Arial", 20))
        self.etiqueta.pack(pady=20)

        # Crea los widgets para elegir el tamaño del tablero y el modo de juego
        self.board_size()
        self.choose_gamemod_2()

        # Añade el botón para comenzar el juego
        self.boton_comenzar = tk.Button(self.master, text="Comenzar", font=("Arial", 16), command=self.comenzar)
        self.boton_comenzar.pack(pady=10)

        # Añade el botón para volver a la ventana anterior
        self.boton_volver = tk.Button(self.master, text="Volver", font=("Arial", 16), command=self.volver)
        self.boton_volver.pack(pady=10)

    def board_size(self):
        # Añade el label y el entry para el tamaño de filas y columnas
        self.frame_size = tk.Frame(self.master)
        self.frame_size.pack(pady=10)
        self.label_size = tk.Label(self.frame_size, text="Tamaño del tablero:", font=("Arial", 16))
        self.label_size.pack(side=tk.LEFT)
        self.entry_size = tk.Entry(self.frame_size, font=("Arial", 16), width=5)
        self.entry_size.pack(side=tk.LEFT)

    def choose_gamemod_2(self):
        #Añade el modo de juego
        self.frame_gamemod_2 = tk.Frame(self.master)
        self.frame_gamemod_2.pack(pady=10)
        self.label_gamemod_2 = tk.Label(self.frame_gamemod_2, text="Modo de juego:", font=("Arial", 16))
        self.label_gamemod_2.pack(side=tk.LEFT)
        self.gamemod_2 = tk.IntVar(value=1)
        self.simple_radius= tk.Radiobutton(self.frame_gamemod_2, text="Modo simple", font=("Arial", 14),
                                           variable=self.gamemod_2, value=1)

        self.simple_radius.pack(side=tk.LEFT)
        self.full_radius = tk.Radiobutton(self.frame_gamemod_2, text="Modo completo", font=("Arial", 14),
                                             variable=self.gamemod_2, value=2)
        self.full_radius.pack(side=tk.LEFT)
        self.simple_radius.select()  # Selecciona el botón de "Modo simple" por defecto

        self.full_radius.pack(side=tk.LEFT)
        self.simple_radius.select()

    def comenzar(self):
        # Obtiene el tamaño del tablero ingresado por el usuario
        size = int(self.entry_size.get())

        # Cierra la ventana actual
        self.master.destroy()

        # Crea la Ventana3 y la muestra
        ventana3 = tk.Toplevel(self.ventana_principal)
        ventana3_gui = Ventana3(ventana3, size, size)

    def volver(self):
        # Cierra la ventana
        self.master.destroy()

        # Muestra la ventana principal
        self.ventana_principal.deiconify()

class Ventana3:
    def __init__(self, master, filas, columnas):
        self.master = master
        self.master.title("Tablero")

        self.create_left_frame("Blue Player", self.volver)
        self.create_board(filas, columnas)
        self.create_right_frame("Red Player", self.iniciar_juego)


    def create_left_frame(self, titulo,comando_volver):

        # Crea un frame para la izquierda de la ventana
        self.left_frame = tk.Frame(self.master, padx=10, pady=10)
        self.left_frame.pack(side="left", fill="y")

        # Crea el título "Blue Player"
        self.titulo_blue = tk.Label(self.left_frame, text=titulo, font=("Arial", 16))
        self.titulo_blue.pack(pady=10)

        # Crea los radio buttons para elegir entre S y O
        self.blue_var = tk.StringVar()
        self.blue_var.set("S")
        self.blue_radio_s = tk.Radiobutton(self.left_frame, text="S", variable=self.blue_var, value="S")
        self.blue_radio_s.pack()
        self.blue_radio_o = tk.Radiobutton(self.left_frame, text="O", variable=self.blue_var, value="O")
        self.blue_radio_o.pack()

        # Añade el botón para volver a la ventana anterior
        self.boton_volver = tk.Button(self.left_frame, text="Volver", font=("Arial", 16), command=self.volver)
        self.boton_volver.pack(side="bottom", pady=10, anchor="sw")

    def create_board(self,filas, columnas):

        # Crea un frame para el tablero
        self.frame_board = tk.Frame(self.master, padx=10, pady=10)
        self.frame_board.pack(side="left")

        # Crea las casillas del tablero
        self.casillas = []
        for i in range(filas):
            fila = []
            for j in range(columnas):
                casilla = tk.Label(self.frame_board, text="", font=("Arial", 32), width=4, height=2, relief="solid", borderwidth=2)
                casilla.grid(row=i, column=j)
                fila.append(casilla)
            self.casillas.append(fila)

    def create_right_frame(self, titulo, comando_iniciar_juego):

        # Crea un frame para la derecha de la ventana
        self.right_frame= tk.Frame(self.master, padx=10, pady=10)
        self.right_frame.pack(side="right", fill="y")

        # Crea el título "Red Player"
        self.titulo_red = tk.Label(self.right_frame, text=titulo, font=("Arial", 16))
        self.titulo_red.pack(pady=10)

        # Crea los radio buttons para elegir entre S y O
        self.red_var = tk.StringVar()
        self.red_var.set("S")
        self.red_radio_s = tk.Radiobutton(self.right_frame, text="S", variable=self.red_var, value="S")
        self.red_radio_s.pack()
        self.red_radio_o = tk.Radiobutton(self.right_frame, text="O", variable=self.red_var, value="O")
        self.red_radio_o.pack()

        # Añade el botón para iniciar el juego
        self.boton_iniciar = tk.Button(self.right_frame, text="Iniciar Juego", font=("Arial", 16), command=self.iniciar_juego)
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
