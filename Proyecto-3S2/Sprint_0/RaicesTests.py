import math
import unittest


class RaicesTests(unittest.TestCase):
    def test_calcularRaizEntero(self):
        esperado = 8.0
        r = Raices()
        calculado = r.calcularRaiz(64.0)
        self.assertEqual(esperado, calculado)

    def test_calcularRaizCero(self):
        esperado = 0.0
        r = Raices()
        calculado = r.calcularRaiz(0.0)
        self.assertEqual(esperado, calculado)

    def test_calcularRaizReal(self):
        self.assertEqual(0.1, Raices().calcularRaiz(0.01))

    def test_calcularRaizNegativo(self):
        self.assertEqual(-999999.0, Raices().calcularRaiz(-6.0))


class Raices:
    def calcularRaiz(self, num):
        if num < 0:
            return -999999.0
        else:
            return math.sqrt(num)


if __name__ == '__main__':
    unittest.main()
