import tkinter as tk
from src.components.Pantalla import Pantalla
from src.components.Boton import Boton

class App(tk.Frame):
  def __init__(self, master = None):
    super().__init__(master)
    self.master = master
    self.create_widgets()
    self.pack()
    
  def create_widgets(self):
    pantalla = Pantalla(self.master)
    pantalla.place(x = 0, y = 0, width = 400, height = 100)
    
    botonLimpiar = Boton(self.master,
                         text = 'C',
                         bg = '#2D2D2F',
                         fg = '#FC6B64',
                         font = ('Arial', 20, 'bold'),
                         command = pantalla.limpiar
                         )
    botonLimpiar.place(x = 0, y = 100, width = 100, height = 100)
    
    botonDividir = Boton(self.master,
                         text = '➗',
                         value = '/',
                         bg = '#2D2D2F',
                         fg = '#63FE7E',
                         font = ('Arial', 20, 'bold'),
                         command = lambda: pantalla.pulsarTecla(tecla = botonDividir.value)
                         )
    botonDividir.place(x = 100, y = 100, width = 100, height = 100)
    
    botonMultiplicar = Boton(self.master,
                             text = '✖',
                             value = '*',
                             bg = '#2D2D2F',
                             fg = '#63FE7E',
                             font = ('Arial', 20, 'bold'),
                             command = lambda: pantalla.pulsarTecla(tecla =botonMultiplicar .value)
                             )
    botonMultiplicar.place(x = 200, y = 100, width = 100, height = 100)
    
    botonRetroceso = Boton(self.master,
                           text = '←',
                           bg = '#2D2D2F',
                           fg = '#63FE7E',
                           font = ('Arial', 20, 'bold'),
                           command = pantalla.retroceso
                           )
    botonRetroceso.place(x = 300, y = 100, width = 100, height = 100)
    
    boton7 = Boton(self.master,
                   text = '7',
                   value = '7',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton7.value)
                   )
    boton7.place(x = 0, y = 200, width = 100, height = 100)
    
    boton8 = Boton(self.master,
                   text = '8',
                   value = '8',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton8.value)
                   )
    boton8.place(x = 100, y = 200, width = 100, height = 100)
    
    boton9 = Boton(self.master,
                   text = '9',
                   value = '9',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton9.value)
                   )
    boton9.place(x = 200, y = 200, width = 100, height = 100)
    
    botonRestar = Boton(self.master,
                        text = '➖',
                        value = '-',
                        bg = '#2D2D2F',
                        fg = '#63FE7E',
                        font = ('Arial', 20, 'bold'),
                        command = lambda: pantalla.pulsarTecla(tecla = botonRestar.value)
                        )
    botonRestar.place(x = 300, y = 200, width = 100, height = 100)
    
    boton4 = Boton(self.master,
                   text = '4',
                   value = '4',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton4.value)
                   )
    boton4.place(x = 0, y = 300, width = 100, height = 100)
    
    boton5 = Boton(self.master,
                   text = '5',
                   value = '5',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton5.value)
                   )
    boton5.place(x = 100, y = 300, width = 100, height = 100)
    
    boton6 = Boton(self.master,
                   text = '6',
                   value = '6',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton6.value)
                   )
    boton6.place(x = 200, y = 300, width = 100, height = 100)
    
    botonSumar = Boton(self.master,
                       text = '➕',
                       value = '+',
                       bg = '#2D2D2F',
                       fg = '#63FE7E',
                       font = ('Arial', 20, 'bold'),
                       command = lambda: pantalla.pulsarTecla(tecla = botonSumar.value)
                       )
    botonSumar.place(x = 300, y = 300, width = 100, height = 100)
    
    boton1 = Boton(self.master,
                   text = '1',
                   value = '1',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton1.value)
                   )
    boton1.place(x = 0, y = 400, width = 100, height = 100)
    
    boton2 = Boton(self.master,
                   text = '2',
                   value = '2',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton2.value)
                   )
    boton2.place(x = 100, y = 400, width = 100, height = 100)
    
    boton3 = Boton(self.master,
                   text = '3',
                   value = '3',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton3.value)
                   )
    boton3.place(x = 200, y = 400, width = 100, height = 100)
    
    botonIgual = Boton(self.master,
                       text = '=',
                       bg = '#318607',
                       fg = '#FBFAFF',
                       font = ('Arial', 20, 'bold'),
                       command = pantalla.evaluarExpresion
                       )
    botonIgual.place(x = 300, y = 400, width = 100, height = 200)
    
    botonDecimal = Boton(self.master,
                         text = ',',
                         value = '.',
                         bg = '#2D2D2F',
                         fg = '#63FE7E',
                         font = ('Arial', 20, 'bold'),
                         command = lambda: pantalla.pulsarTecla(tecla = botonDecimal.value)
                         )
    botonDecimal.place(x = 0, y = 500, width = 100, height = 100)
    
    boton0 = Boton(self.master,
                   text = '0',
                   value = '0',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold'),
                   command = lambda: pantalla.pulsarTecla(tecla = boton0.value)
                   )
    boton0.place(x = 100, y = 500, width = 100, height = 100)
    
    boton00 = Boton(self.master,
                    text = '00',
                    value = '00',
                    bg = '#171719',
                    fg = '#EAEAEA',
                    font = ('Arial', 20, 'bold'),
                    command = lambda: pantalla.pulsarTecla(tecla = boton00.value)
                    )
    boton00.place(x = 200, y = 500, width = 100, height = 100)