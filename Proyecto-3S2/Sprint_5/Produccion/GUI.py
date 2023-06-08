import time
import tkinter as tk
from Board import *
from Computer import *
from tkinter import messagebox

class Ventana1:

    def __init__(self, master):
        self.master = master
        self.master.title("S O S")
        self.master.configure(bg="#E6E6FA")
        # Añade widgets a la ventana
        self.etiqueta = tk.Label(self.master, text="Bienvenido a S O S", bg="#E6E6FA", font=("Courier", 20))
        self.etiqueta.pack(pady=20)
        # Refac. botones
        botones_config = [
            {
                "text": "P vs PC",
                "command": self.singleplayer
            },
            {
                "text": "P vs P",
                "command": self.multiplayer
            },
            {
                "text": 'PC vs PC',
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
        Ventana2(ventana2, self.master, "P vs PC")

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
        Ventana2(ventana2, self.master, "PC vs PC")

    def salir(self):
        # Cierra la ventana principal
        self.master.destroy()

class Ventana2:

    def __init__(self, master, v_principal, gamemode_1):
        self.master = master
        self.ventana_principal = v_principal
        self.player_selection = 0
        self.frame_size = None
        self.entry_size = None
        self.frame_player = None
        self.frame_gamemod_2 = None
        self.gamemod_2 = None
        # Inicializa con valor predeterminado si no es P vs P
        self.players = None if gamemode_1 != "P vs P" else tk.StringVar(value="P vs P")

        self.master.title(gamemode_1)
        self.master.configure(bg="#E6E6FA")
        self.master.gamemode_1 = gamemode_1
        self.etiqueta = tk.Label(self.master, text=f" {gamemode_1}", font=("Courier", 18), bg="#E6E6FA")
        self.etiqueta.pack(pady=12)
        self.board_size()

        if gamemode_1 == 'P vs PC':
            self.choose_player()

        self.choose_gamemod_2()
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

    def choose_player(self):
        # Crea el frame para elegir el jugador
        self.frame_player = tk.Frame(self.master, bg="#E6E6FA", pady=10)
        self.frame_player.pack()

        # Crea el label para elegir el jugador
        tk.Label(self.frame_player, text="Elige tu jugador:", font=("Courier", 14), bg="#E6E6FA").pack(side=tk.LEFT)

        # Crea las variables para el jugador
        self.players = tk.StringVar(value='0')

        # Crea los botones de radio para elegir el jugador
        tk.Radiobutton(self.frame_player, text="Blue Player", font=("Courier", 13), bg="#E6E6FA",
                       variable=self.players, value="Blue Player").pack(side=tk.LEFT)
        tk.Radiobutton(self.frame_player, text="Red Player", font=("Courier", 13), bg="#E6E6FA",
                       variable=self.players, value="Red Player").pack(side=tk.LEFT)

    def choose_gamemod_2(self):
        # Crea el frame para el modo de juego
        self.frame_gamemod_2 = tk.Frame(self.master, bg="#E6E6FA", pady=10)
        self.frame_gamemod_2.pack()
        # Crea el label para el modo de juego
        tk.Label(self.frame_gamemod_2, text="Modo de juego:", font=("Courier", 14), bg="#E6E6FA").pack(side=tk.LEFT)
        # Crea las variables para el modo de juego
        self.gamemod_2 = tk.IntVar(value=0)
        # Crea los botones de radio para el modo de juego
        tk.Radiobutton(self.frame_gamemod_2, text="Modo simple", font=("Courier", 13),
                       bg="#E6E6FA", variable=self.gamemod_2, value=1).pack(side=tk.LEFT)
        tk.Radiobutton(self.frame_gamemod_2, text="Modo general", font=("Courier", 13),
                       bg="#E6E6FA", variable=self.gamemod_2, value=2).pack(side=tk.LEFT)

    def comenzar(self):
        # Obtiene el tamaño del tablero ingresado por el usuario
        try:
            size = int(self.entry_size.get())
            if size <= 2 or size > 16:
                raise ValueError
        except ValueError:
            # Muestra una ventana emergente con el mensaje de error
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
        if self.master.gamemode_1 == "P vs P":
            self.player_selection = "P vs P"
        elif self.master.gamemode_1 == "P vs PC":
            if self.players is None:
                messagebox.showinfo("Advertencia", "Por favor, elige un jugador.")
                return
            self.player_selection = self.players.get()
        else:
            self.player_selection = None
        # Cierra la ventana actual
        self.master.destroy()
        # Crea la Ventana3 y la muestra
        ventana3 = tk.Toplevel(self.ventana_principal)
        Ventana3(ventana3, size, size, self.master.gamemode_1, gamemode_2, self.player_selection)

    def volver(self):
        # Cierra la ventana
        self.master.destroy()
        # Muestra la ventana principal
        self.ventana_principal.deiconify()

class Ventana3:
    def __init__(self, master, filas, columnas, gamemode_1, gamemode_2, player_selection):
        self.player_selection = player_selection
        self.left_letter = tk.IntVar(value=-1)
        self.right_letter = tk.IntVar(value=-1)
        self.left_sos_created_label = None
        self.right_sos_created_label = None
        self.left_frame = None
        self.right_frame = None
        self.boton_volver = None
        self.board_frame = None
        self.canvas_board = None
        self.boton_nuevo_juego = None
        self.turn_frame = None
        self.turn_label = None
        self.is_computer_playing = False
        self.master = master
        self.gamemode_1 = gamemode_1
        self.gamemode_2 = gamemode_2
        self.filas=filas
        self.columnas=columnas
        self.valor_sos_creados_1 = None
        self.valor_sos_creados_2 = None
        self.resultado = None

        if gamemode_2 == 'Simple':
            self.master.title("Tablero modo simple")
        elif gamemode_2 == 'General':
            self.master.title("Tablero modo general")

        self.master.board = Board(gamemode_1, gamemode_2, filas)
        self.canvas_size = 400
        self.cell_size = self.canvas_size / self.master.board.size
        self.isGameOver = False

        # Frame izquierdo, titulo
        if gamemode_1 == 'PC vs PC':
            self.left_name = "Computer A"
            self.is_computer_playing = True
        elif gamemode_1 == 'P vs PC':
            self.left_name = "Blue Player" if self.player_selection == "Blue Player" else "Computer"
            self.is_computer_playing = True if self.player_selection == "Red Player" else False
        else:
            self.left_name = "Blue Player"
        self.create_left_frame(self.left_name, self.volver)

        # Frame derecho, titulo
        if gamemode_1 == 'PC vs PC':
            self.right_name = "Computer B"
        elif gamemode_1 == 'P vs PC':
            self.right_name = "Computer" if self.player_selection == "Blue Player" else "Red Player"
        else:
            self.right_name = "Red Player"
        self.create_right_frame(self.right_name)

        self.create_board(filas, columnas)
        self.create_turn_label()
        self.update_turn_label()

        # Iniciar computadora(s)
        if gamemode_1 == 'PC vs PC':
            self.computer_A = Computer(gamemode_1, gamemode_2, filas)
            self.computer_B = Computer(gamemode_1, gamemode_2, filas)
            self.start_computer_game()
        elif gamemode_1 == 'P vs PC':
            self.computer = Computer(gamemode_1, gamemode_2, filas)
            if self.left_name == 'Computer':
                self.start_computer_turn()

    def create_player_frame(self, frame, titulo, variable, enabled=True):
        # Crea el título del jugador
        titulo_label = tk.Label(frame, text=titulo, font=("Courier", 15), bg="#E6E6FA")
        titulo_label.pack(pady=10)
        # Crea los radio buttons para elegir entre S y O
        variable.set("S")
        radio_s = tk.Radiobutton(frame, text="S", variable=variable, value="S", bg="#E6E6FA")
        radio_s.pack()
        radio_o = tk.Radiobutton(frame, text="O", variable=variable, value="O", bg="#E6E6FA")
        radio_o.pack()
        # Deseleccionar los botones de radio
        variable.set(-1)
        # Deshabilitar para computadora
        if not enabled:
            radio_s.configure(state='disabled')
            radio_o.configure(state='disabled')
        # SOS creados
        if self.master.board.gamemode_2 == 'General':
            label = tk.Label(frame, text="SOS created: 0", font=("Courier", 15), bg="#E6E6FA")
            label.pack(pady=10)
            return label

    def create_left_frame(self, titulo, comando_volver):
        # Crea un frame para la izquierda de la ventana
        self.left_frame = tk.Frame(self.master, padx=10, pady=10, bg="#E6E6FA")
        self.left_frame.pack(side="left", fill="y")
        self.left_letter = tk.StringVar()
        self.left_sos_created_label = self.create_player_frame(self.left_frame, titulo,
                                                               self.left_letter, 'Player' in self.left_name)
        # Añade el botón para volver a la ventana anterior
        self.boton_volver = tk.Button(self.left_frame, text="Volver", font=("Courier", 13),
                                      bg="#89AC76", command=comando_volver)
        self.boton_volver.pack(side="bottom", pady=10, anchor="sw")

    def create_board(self, filas, columnas):
        # Crea un marco para contener el tablero
        self.board_frame = tk.Frame(self.master, bg="#E6E6FA")
        self.board_frame.pack(side="left", fill="both", expand=True)
        # Crea un canvas para el tablero dentro del marco
        self.canvas_board = tk.Canvas(self.board_frame, width=self.canvas_size, height=self.canvas_size, bg="#E6E6FA")
        self.canvas_board.pack()
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
        self.right_frame = tk.Frame(self.master, padx=10, pady=10, bg="#E6E6FA")
        self.right_frame.pack(side="right", fill="y")
        self.right_letter = tk.StringVar()
        self.right_sos_created_label = self.create_player_frame(self.right_frame, titulo,
                                                                self.right_letter, 'Player' in self.right_name)
        #AGREGUE ESTO AHORA
        self.boton_guardar_juego = tk.Button(self.right_frame, text="Guardar Juego", font=("Courier", 13), bg="#89AC76",
                                             command=self.guardar_juego)
        self.boton_guardar_juego.pack(side=tk.BOTTOM, pady=10)


    def create_turn_label(self):
        # Crea un frame contenedor en el mismo marco que el tablero
        self.turn_frame = tk.Frame(self.board_frame, bg="#89AC76")
        self.turn_frame.pack(side=tk.BOTTOM, pady=10)
        # Crea el label del turno dentro del frame contenedor
        self.turn_label = tk.Label(self.turn_frame, text="", font=("Courier", 12), bg="#89AC76")
        self.turn_label.grid(row=1, column=0, pady=10)

    def update_turn_label(self):
        # Actualiza el texto del label del turno con el jugador correspondiente
        turn = self.master.board.turn
        player = self.left_name if turn == 'left' else self.right_name
        self.is_computer_playing = True if 'Computer' in player else False
        self.turn_label.config(text=f'Turno de {player}')

    def add_letter(self, event):
        if not self.isGameOver and not self.is_computer_playing:
            # calcular fila y columna a partir de las coordenadas del evento
            row = int(event.y / self.cell_size)
            col = int(event.x / self.cell_size)
            # obtener letra y turno
            turn = self.master.board.turn
            letter = None
            if turn == 'left' and self.left_letter.get() != "-1":
                letter = self.left_letter.get()
            elif turn == 'right' and self.right_letter.get() != "-1":
                letter = self.right_letter.get()
            if letter is not None:
                # añadir letra a la casilla correspondiente
                self.add_letter_board(letter, row, col)
                if (self.master.board.turn == 'left' and 'Computer' in self.left_name) or \
                        (self.master.board.turn == 'right' and 'Computer' in self.right_name):
                    self.is_computer_playing = True
                    self.start_computer_turn()

    def add_letter_board(self, letter, row, col):
        if self.master.board.add_letter(letter, row, col):
            # obtener la coordenada (x, y) de la esquina superior izquierda de la casilla
            x0 = col * self.cell_size
            y0 = row * self.cell_size
            # dibujar la letra en la casilla correspondiented
            self.canvas_board.create_text(x0 + self.cell_size / 2, y0 + self.cell_size / 2,
                                          text=letter, fill="black")
            createdSOS = self.check_and_draw_SOS(letter, row, col)
            result = self.master.board.checkVictory()
            if result is not None:
                self.mostrarGanador()
            elif not createdSOS:
                self.master.board.change_turn()
                self.update_turn_label()
            if self.master.board.gamemode_1 == 'P vs PC' and self.master.board.gamemode_2 == 'General':
                if (self.master.board.turn == 'left' and 'Computer' in self.left_name) or \
                        (self.master.board.turn == 'right' and 'Computer' in self.right_name):
                    self.start_computer_turn()  # Iniciar el siguiente turno de la computadora

            if self.master.board.gamemode_2 == 'General':
                self.left_sos_created_label.config(text=f"SOS created: {self.master.board.SOS_created['left']}")
                self.right_sos_created_label.config(text=f"SOS created: {self.master.board.SOS_created['right']}")

                self.valor_sos_creados_1 = str(self.master.board.SOS_created['left'])
                self.valor_sos_creados_2 = str(self.master.board.SOS_created['right'])

        else:
            # La casilla ya está ocupada
            tk.messagebox.showerror("Error", "Esta casilla ya está ocupada")

        self.update_turn_label()

    def check_and_draw_SOS(self, letter, x, y):
        createdSOS, SOS = self.master.board.check_SOS(letter, x, y)
        if createdSOS:
            for s in SOS:
                x1, y1 = s[0][1] * self.cell_size + self.cell_size / 2, s[0][0] * self.cell_size + self.cell_size / 2
                x2, y2 = s[1][1] * self.cell_size + self.cell_size / 2, s[1][0] * self.cell_size + self.cell_size / 2
                color = 'Blue' if self.master.board.turn == 'left' else 'Red'
                self.canvas_board.create_line(x1, y1, x2, y2, fill=color)
            self.update_turn_label()  # Agregar esta línea para actualizar el turn_label

        return createdSOS

    def mostrarGanador(self):
        resultado = self.master.board.checkVictory()
        if resultado is None:
            messagebox.showinfo("Sin ganador", "El juego aún no ha terminado.")
        else:
            self.isGameOver = True
            if resultado == 'left':
                messagebox.showinfo("Ganador", f"¡{self.left_name} ha ganado!")
            elif resultado == 'right':
                messagebox.showinfo("Ganador", f"¡{self.right_name} ha ganado!")
            elif resultado == "Draw":
                messagebox.showinfo("Empate", "¡El juego ha terminado en empate!")

            self.resultado = str(resultado)

    def start_computer_turn(self):
        play = self.computer.play_turn(self.master.board.cells)
        letter = play[0]
        row, col = play[1][0], play[1][1]
        self.add_letter_board(letter, row, col)
        self.is_computer_playing = False
        self.update_turn_label()  # Actualizar el turn_label después de establecer is_computer_playing en False

    def start_computer_game(self):
        if not self.isGameOver:
            actual_computer = self.computer_A if self.master.board.turn == 'left' else self.computer_B
            play = actual_computer.play_turn(self.master.board.cells)
            letter = play[0]
            row, col = play[1][0], play[1][1]
            self.add_letter_board(letter, row, col)

            # Verificar si el juego ha terminado
            if self.isGameOver:
                return

            # Llamar a start_computer_game después de un cierto tiempo
            self.master.after(100, self.start_computer_game)

    def guardar_juego(self):
        filename = "movimientos.txt"  # Nombre del archivo de destino
        messagebox.showinfo("Atención", "Se grabarán los movimientos en el archivo 'movimientos.txt'.")
        result = self.master.board.record_game(filename)

        if result == "Game recorded successfully.":
            messagebox.showinfo("Guardado", "El juego se ha guardado exitosamente en el archivo 'movimientos.txt'.")
        else:
            messagebox.showerror("Error", "Error al guardar el juego: " + result)

        # Escribir las variables en el archivo existente
        archivo = open("movimientos.txt", "a+")
        archivo.write("\nSOS Izquierdos: "+self.valor_sos_creados_1 + "\n")
        archivo.write("SOS Derechos: "+self.valor_sos_creados_2 + "\n\n")

        if self.resultado == "left":
            archivo.write("El ganador es: " + self.left_name)
        if self.resultado == "right":
            archivo.write("El ganador es: " + self.right_name)
        elif self.resultado == "Draw":
            archivo.write("El resultado del juego es empate")
        archivo.close()

    def volver(self):
        # Cierra la ventana actual
        self.master.destroy()
        # Muestra la ventana anterior
        self.master.master.deiconify()

# Crea la ventana principal
ventana_principal = tk.Tk()
ventana_principal.geometry("400x400")
# Muestra la primera ventana
ventana1 = Ventana1(ventana_principal)
# Mantiene la ventana principal en bucle
ventana_principal.mainloop()
