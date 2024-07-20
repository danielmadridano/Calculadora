import unittest
import tkinter as tk
from src.components.Pantalla import Pantalla

class TestPantalla(unittest.TestCase):
    def setUp(self):
      self.root = tk.Tk()
      self.pantalla = Pantalla(self.root)

    def tearDown(self):
      self.root.destroy()

    def test_init(self):
      self.assertIsInstance(self.pantalla, tk.Entry)
      self.assertEqual(self.pantalla.expresion, '')
      self.assertEqual(self.pantalla.resultado, '')

    def test_limpiar(self):
      self.pantalla.entryExpresion.insert(0, '123')
      self.pantalla.entryResultado.insert(0, '456')
      self.pantalla.expresion = '123'
      self.pantalla.resultado = '456'
      self.pantalla.limpiar()
      self.assertEqual(self.pantalla.entryExpresion.get(), '')
      self.assertEqual(self.pantalla.entryResultado.get(), '')
      self.assertEqual(self.pantalla.expresion, '')
      self.assertEqual(self.pantalla.resultado, '')

    def test_pulsarTecla(self):
      self.pantalla.pulsarTecla('1')
      self.assertEqual(self.pantalla.entryExpresion.get(), '1')
      self.assertEqual(self.pantalla.expresion, '1')
      
    def test_number_after_result(self):
      self.pantalla.expresion = '1+2'
      self.pantalla.evaluarExpresion()
      self.pantalla.pulsarTecla('4')
      self.assertEqual(self.pantalla.expresion, '4')

    def test_evaluarExpresion(self):
      self.pantalla.expresion = '2+3'
      self.pantalla.evaluarExpresion()
      self.assertEqual(self.pantalla.entryResultado.get(), '5')
      self.assertEqual(self.pantalla.resultado, '5')
      
    def test_SyntaxError(self):
      self.pantalla.expresion = '1+'
      self.pantalla.evaluarExpresion()
      self.assertEqual(self.pantalla.entryResultado.get(), 'Syntax Error')
      self.assertEqual(self.pantalla.resultado, '')
      
    def test_MathError(self):
      self.pantalla.expresion = '1/0'
      self.pantalla.evaluarExpresion()
      self.assertEqual(self.pantalla.entryResultado.get(), 'Math Error')
      self.assertEqual(self.pantalla.resultado, '')
        
    def test_retroceso(self):
      self.pantalla.expresion = '123'
      self.pantalla.entryExpresion.insert(0, '123')
      self.pantalla.retroceso()
      self.assertEqual(self.pantalla.expresion, '12')
      self.assertEqual(self.pantalla.entryExpresion.get(), '12')

if __name__ == "__main__":
    unittest.main()