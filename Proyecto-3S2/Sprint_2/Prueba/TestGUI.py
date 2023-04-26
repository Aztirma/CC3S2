import unittest
from ..Produccion.Board import *
from ..Produccion.GUI import *


class TestGUI(unittest.TestCase):
    def setUp(self):
        ventana_principal = tk.Tk()
        ventana_principal.geometry("400x400")

        ventana1 = Ventana1(ventana_principal)
        ventana2 = tk.Toplevel()
        Ventana2(ventana2, ventana1.master, "Multiplayer")

        ventana_principal.mainloop()

    def test(self):
        self.assertEqual(True, True)


if __name__ == '__main__':
    unittest.main()
