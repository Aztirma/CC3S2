import tkinter as tk
from Board import *
from tkinter import messagebox

class Ventana1:

    def __init__(self, master):
        self.master = master
        self.master.title("S O S")
        self.master.configure(bg="#E6E6FA")

        # Añade widgets a la ventana
        self.etiqueta = tk.Label(self.master, text="Bienvenido a S O S", bg="#E6E6FA", font=("Courier", 20))
        self.etiqueta.pack(pady=20)

        #Refac. botones
        botones_config = [
            {
                "text": "P vs E",
                "command": self.singleplayer
            },
            {
                "text": "P vs P",
                "command": self.multiplayer
            },
            {
                "text": "E vs E",
                "command": self.computer
            },
            {
                "text": "Salir",
                "command": self.salir
            }
        ]

        for config in botones_config:
            boton = tk.Button(self.master, text=config["text"], bg="#89AC76", font=("Courier", 16),
                              command=config["command"], width=10)
            boton.pack(pady=10)

    def singleplayer(self):
        # Oculta la ventana principal
        self.master.withdraw()

        # Crea la segunda ventana utilizando Toplevel
        ventana2 = tk.Toplevel()
        Ventana2(ventana2, self.master, "P vs E")

    def multiplayer(self):
        # Oculta la ventana principal
        self.master.withdraw()

        # Crea la segunda ventana utilizando Toplevel
        ventana2 = tk.Toplevel()
        Ventana2(ventana2, self.master, "P vs P")

    def computer(self):
        # Oculta la ventana principal
        self.master.withdraw()

        # Crea la segunda ventana utilizando Toplevel
        ventana2 = tk.Toplevel()
        Ventana2(ventana2, self.master, "E vs E")

    def salir(self):
        # Cierra la ventana principal
        self.master.destroy()

class Ventana2:

    def __init__(self, master, ventana_principal, gamemode_1):
        self.master = master
        self.master.title(gamemode_1)
        self.master.configure(bg="#E6E6FA")
        self.master.gamemode_1 = gamemode_1
        self.ventana_principal = ventana_principal

        # Añade widgets a la ventana
        self.etiqueta = tk.Label(self.master, text=f" {gamemode_1}", font=("Courier", 18), bg="#E6E6FA")
        self.etiqueta.pack(pady=12)

        # Crea los widgets para elegir el tamaño del tablero y el modo de juego
        self.board_size()
        self.choose_gamemod_2()

        #botones
        botones_config_2 = [
            {
                "text": "Comenzar",
                "command": self.comenzar
            },
            {
                "text": "Volver",
                "command": self.volver
            }
        ]

        for config in botones_config_2:
            boton = tk.Button(self.master, text=config["text"], font=("Courier", 15), bg="#89AC76",
                              command=config["command"], width=10)
            boton.pack(pady=10)

    def board_size(self):
        # Crea el frame para el tamaño del tablero
        self.frame_size = tk.Frame(self.master, pady=10,  bg="#E6E6FA")
        self.frame_size.pack()

        # Crea el label y la entrada para el tamaño del tablero
        tk.Label(self.frame_size, text="Tamaño del tablero:", font=("Courier", 15), bg="#E6E6FA").pack(side=tk.LEFT)
        self.entry_size = tk.Entry(self.frame_size, font=("Courier", 15), width=5)
        self.entry_size.pack(side=tk.LEFT)

    def choose_gamemod_2(self):
        # Crea el frame para el modo de juego
        self.frame_gamemod_2 = tk.Frame(self.master, bg="#E6E6FA", pady=10)
        self.frame_gamemod_2.pack()

        # Crea el label para el modo de juego
        tk.Label(self.frame_gamemod_2, text="Modo de juego:", font=("Courier", 14), bg="#E6E6FA").pack(side=tk.LEFT)

        # Crea las variables para el modo de juego
        self.gamemod_2 = tk.IntVar(value=0)

        # Crea los botones de radio para el modo de juego
        tk.Radiobutton(self.frame_gamemod_2, text="Modo simple", font=("Courier", 13), bg="#E6E6FA",
                       variable=self.gamemod_2, value=1).pack(side=tk.LEFT)
        tk.Radiobutton(self.frame_gamemod_2, text="Modo general", font=("Courier", 13), bg="#E6E6FA",
                       variable=self.gamemod_2, value=2).pack(side=tk.LEFT)

    def comenzar(self):
        # Obtiene el tamaño del tablero ingresado por el usuario
        try:
            size = int(self.entry_size.get())
            if size <= 2 or size > 16:
                raise ValueError
        except ValueError:
            #Muestra una ventana emergente con el mensaje de error
            messagebox.showerror("Error", "¡El tamaño del tablero debe ser un número entero mayor a 2!")
            return

        selected_option = int(self.gamemod_2.get())
        if selected_option == 1:
            gamemode_2 = 'Simple'
        elif selected_option == 2:
            gamemode_2 = 'General'
        else:
            messagebox.showinfo("Advertencia", "Por favor, elige un modo de juego.")
            return

        # Cierra la ventana actual
        self.master.destroy()

        # Crea la Ventana3 y la muestra
        ventana3 = tk.Toplevel(self.ventana_principal)
        ventana3_gui = Ventana3(ventana3, size, size, self.master.gamemode_1, gamemode_2)

    def volver(self):
        # Cierra la ventana
        self.master.destroy()

        # Muestra la ventana principal
        self.ventana_principal.deiconify()

class Ventana3:
    def __init__(self, master, filas, columnas, gamemode_1, gamemode_2):
        self.red_var = None
        self.blue_var = None
        self.red_sos_created_label = None
        self.blue_sos_created_label = None
        self.master = master
        self.gamemode_1=gamemode_1
        if gamemode_2 == 'Simple':
            self.master.title("Tablero modo simple")
        elif gamemode_2 == 'General':
            self.master.title("Tablero modo general")
        self.master.board = Board(gamemode_1, gamemode_2, filas)

        self.canvas_size = 400
        self.cell_size = self.canvas_size / self.master.board.size
        self.isGameOver = False

        self.create_left_frame("Blue Player", self.volver)
        self.create_board(filas, columnas)

        #Frame derecho, titulo
        if gamemode_1 == 'P vs E':
            titulo = "Computer"
        else:
            titulo = "Red Player"
        self.create_right_frame(titulo)

        self.create_turn_label()
        self.update_turn_label()

    def create_player_frame(self, frame, titulo, variable, label):
        # Crea el título del jugador
        titulo_label = tk.Label(frame, text=titulo, font=("Courier", 15), bg="#E6E6FA")
        titulo_label.pack(pady=10)

        # Crea los radio buttons para elegir entre S y O
        variable.set("S")
        radio_s = tk.Radiobutton(frame, text="S", variable=variable, value="S", bg="#E6E6FA")
        radio_s.pack()
        radio_o = tk.Radiobutton(frame, text="O", variable=variable, value="O", bg="#E6E6FA")
        radio_o.pack()

        # SOS creados
        if self.master.board.gamemode_2 == 'General':
            label = tk.Label(frame, text="SOS created: 0", font=("Courier", 15), bg="#E6E6FA")
            label.pack(pady=10)
            return label

    def create_left_frame(self, titulo, comando_volver):

        # Crea un frame para la izquierda de la ventana
        self.left_frame = tk.Frame(self.master, padx=10, pady=10, bg="#E6E6FA")
        self.left_frame.pack(side="left", fill="y")

        self.blue_var = tk.StringVar()
        self.blue_sos_created_label = self.create_player_frame(self.left_frame, titulo, self.blue_var,
                                                               self.blue_sos_created_label)

        # Añade el botón para volver a la ventana anterior
        self.boton_volver = tk.Button(self.left_frame, text="Volver", font=("Courier", 14), bg="#89AC76", command=comando_volver)
        self.boton_volver.pack(side="bottom", pady=10, anchor="sw")

    def create_board(self, filas, columnas):
        # Crea un canvas para el tablero
        self.canvas_board = tk.Canvas(self.master, width=self.canvas_size, height=self.canvas_size,bg="#E6E6FA")
        self.canvas_board.pack(side="left")

        # Dibuja las líneas del tablero
        for i in range(1, filas):
            y = i * self.canvas_size / filas
            self.canvas_board.create_line(0, y, 400, y)
        for j in range(1, columnas):
            x = j * self.canvas_size / columnas
            self.canvas_board.create_line(x, 0, x, 400)

        # Añade evento "click" al canvas
        self.canvas_board.bind("<Button-1>", self.add_letter)

    def create_right_frame(self, titulo):
        # Crea un frame para la derecha de la ventana
        self.right_frame= tk.Frame(self.master, padx=10, pady=10,bg="#E6E6FA")
        self.right_frame.pack(side="right", fill="y")

        self.red_var = tk.StringVar()
        self.red_sos_created_label = self.create_player_frame(self.right_frame, titulo, self.red_var,
                                                              self.red_sos_created_label)

    def create_turn_label(self):
        # Crea un frame contenedor en la esquina inferior derecha del tablero
        self.turn_frame = tk.Frame(self.right_frame,bg="#89AC76")
        self.turn_frame.pack(side=tk.RIGHT, anchor=tk.SE)

        # Crea el label del turno dentro del frame contenedor
        self.turn_label = tk.Label(self.turn_frame, text="", font=("Courier", 12), bg="#89AC76")
        self.turn_label.pack(side=tk.BOTTOM, pady=10)

    def update_turn_label(self):
        # Actualiza el texto del label del turno con el jugador correspondiente
        gamemode_1 = self.gamemode_1
        turn = self.master.board.turn
        if gamemode_1 == 'P vs E':
            if turn == 'Blue':
                player = "Computer"
            else:
                player = "Red Player"
            self.turn_label.config(text=f"Turno de {player}")
        else:
            if turn == 'Blue':
                player = "Blue"
            else:
                player = "Red Player"
            self.turn_label.config(text=f"Turno de {player}")

    def add_letter(self, event):
        if not self.isGameOver:
            # calcular fila y columna a partir de las coordenadas del evento
            row = int(event.y / self.cell_size)
            col = int(event.x / self.cell_size)

            # obtener letra y turno
            turn = self.master.board.turn
            letter = self.blue_var.get() if turn == 'Blue' else self.red_var.get()

            # añadir letra a la casilla correspondiente
            if self.master.board.add_letter(letter, row, col):
                # obtener la coordenada (x, y) de la esquina superior izquierda de la casilla
                x0 = col * self.cell_size
                y0 = row * self.cell_size
                # dibujar la letra en la casilla correspondiente
                self.canvas_board.create_text(x0 + self.cell_size / 2, y0 + self.cell_size / 2, text=letter, fill="black")
                createdSOS = self.check_and_draw_SOS(letter, row, col)
                result = self.master.board.checkVictory()
                if result is not None:
                    self.mostrarGanador()
                elif not createdSOS:
                    self.master.board.change_turn()
            else:
                # La casilla ya está ocupada
                tk.messagebox.showerror("Error", "Esta casilla ya está ocupada")

            # actualizar etiqueta de turno
            self.update_turn_label()
            if self.master.board.gamemode_2 == 'General':
                self.blue_sos_created_label.config(text=f"SOS created: {self.master.board.SOS_created['Blue']}")
                self.red_sos_created_label.config(text=f"SOS created: {self.master.board.SOS_created['Red']}")

    def check_and_draw_SOS(self, letter, x, y):
        createdSOS, SOS = self.master.board.check_SOS(letter, x, y)
        if createdSOS:
            for s in SOS:
                x1, y1 = s[0][1] * self.cell_size + self.cell_size / 2, s[0][0] * self.cell_size + self.cell_size / 2
                x2, y2 = s[1][1] * self.cell_size + self.cell_size / 2, s[1][0] * self.cell_size + self.cell_size / 2
                color = self.master.board.turn.lower()
                self.canvas_board.create_line(x1, y1, x2, y2, fill=color)
        return createdSOS

    def mostrarGanador(self):
        resultado = self.master.board.checkVictory()
        if resultado is None:
            messagebox.showinfo("Sin ganador", "El juego aún no ha terminado.")
        else:
            self.isGameOver = True
            if resultado == 'Blue':
                messagebox.showinfo("Ganador", "¡Blue Player ha ganado!")
            elif resultado == 'Red':
                messagebox.showinfo("Ganador", "¡Red Player ha ganado!")
            elif resultado == "Draw":
                messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")

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
