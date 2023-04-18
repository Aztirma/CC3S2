import tkinter as tk


class GUI:
    def __init__(self):
        # Titulo de la ventana
        self.window = tk.Tk()
        self.window.title("Tic Tac Toe")

        # Tablero
        self.canvas = tk.Canvas(self.window, width=300, height=300)
        self.canvas.pack()
        self.canvas.create_line(0, 100, 300, 100)
        self.canvas.create_line(0, 200, 300, 200)
        self.canvas.create_line(100, 0, 100, 300)
        self.canvas.create_line(200, 0, 200, 300)

        # Checkbox
        self.checkbox_var = tk.BooleanVar()
        self.checkbox = tk.Checkbutton(self.window, text="Habilitar sonido", variable=self.checkbox_var)
        self.checkbox.pack()

        # Dificultad
        self.radio_var = tk.StringVar()
        self.radio_var.set("facil")
        self.easy_radio = tk.Radiobutton(self.window, text="Fácil", variable=self.radio_var, value="facil")
        self.medium_radio = tk.Radiobutton(self.window, text="Normal", variable=self.radio_var, value="normal")
        self.hard_radio = tk.Radiobutton(self.window, text="Difícil", variable=self.radio_var, value="dificil")
        self.easy_radio.pack()
        self.medium_radio.pack()
        self.hard_radio.pack()

        # Iniciar partida
        self.button = tk.Button(self.window, text="Iniciar partida", command=self.iniciar_partida)
        self.button.pack()

    def iniciar_partida(self):
        pass


gui = GUI()
gui.window.mainloop()
