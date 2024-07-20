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
                         font = ('Arial', 20, 'bold')
                         )
    botonLimpiar.place(x = 0, y = 100, width = 100, height = 100)
    
    botonDividir = Boton(self.master,
                         text = '➗',
                         value = '/',
                         bg = '#2D2D2F',
                         fg = '#63FE7E',
                         font = ('Arial', 20, 'bold')
                         )
    botonDividir.place(x = 100, y = 100, width = 100, height = 100)
    
    botonMultiplicar = Boton(self.master,
                             text = '✖',
                             value = '*',
                             bg = '#2D2D2F',
                             fg = '#63FE7E',
                             font = ('Arial', 20, 'bold')
                             )
    botonMultiplicar.place(x = 200, y = 100, width = 100, height = 100)
    
    botonRetroceso = Boton(self.master,
                           text = '←',
                           bg = '#2D2D2F',
                           fg = '#63FE7E',
                           font = ('Arial', 20, 'bold')
                           )
    botonRetroceso.place(x = 300, y = 100, width = 100, height = 100)
    
    boton7 = Boton(self.master,
                   text = '7',
                   value = '7',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton7.place(x = 0, y = 200, width = 100, height = 100)
    
    boton8 = Boton(self.master,
                   text = '8',
                   value = '8',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton8.place(x = 100, y = 200, width = 100, height = 100)
    
    boton9 = Boton(self.master,
                   text = '9',
                   value = '9',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton9.place(x = 200, y = 200, width = 100, height = 100)
    
    botonRestar = Boton(self.master,
                        text = '➖',
                        value = '-',
                        bg = '#2D2D2F',
                        fg = '#63FE7E',
                        font = ('Arial', 20, 'bold')
                        )
    botonRestar.place(x = 300, y = 200, width = 100, height = 100)
    
    boton4 = Boton(self.master,
                   text = '4',
                   value = '4',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton4.place(x = 0, y = 300, width = 100, height = 100)
    
    boton5 = Boton(self.master,
                   text = '5',
                   value = '5',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton5.place(x = 100, y = 300, width = 100, height = 100)
    
    boton6 = Boton(self.master,
                   text = '6',
                   value = '6',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton6.place(x = 200, y = 300, width = 100, height = 100)
    
    botonSumar = Boton(self.master,
                       text = '➕',
                       value = '+',
                       bg = '#2D2D2F',
                       fg = '#63FE7E',
                       font = ('Arial', 20, 'bold')
                       )
    botonSumar.place(x = 300, y = 300, width = 100, height = 100)
    
    boton1 = Boton(self.master,
                   text = '1',
                   value = '1',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton1.place(x = 0, y = 400, width = 100, height = 100)
    
    boton2 = Boton(self.master,
                   text = '2',
                   value = '2',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton2.place(x = 100, y = 400, width = 100, height = 100)
    
    boton3 = Boton(self.master,
                   text = '3',
                   value = '3',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton3.place(x = 200, y = 400, width = 100, height = 100)
    
    botonIgual = Boton(self.master,
                       text = '=',
                       bg = '#318607',
                       fg = '#FBFAFF',
                       font = ('Arial', 20, 'bold')
                       )
    botonIgual.place(x = 300, y = 400, width = 100, height = 200)
    
    botonDecimal = Boton(self.master,
                         text = ',',
                         value = '.',
                         bg = '#2D2D2F',
                         fg = '#63FE7E',
                         font = ('Arial', 20, 'bold')
                         )
    botonDecimal.place(x = 0, y = 500, width = 100, height = 100)
    
    boton0 = Boton(self.master,
                   text = '0',
                   value = '0',
                   bg = '#171719',
                   fg = '#EAEAEA',
                   font = ('Arial', 20, 'bold')
                   )
    boton0.place(x = 100, y = 500, width = 100, height = 100)
    
    boton00 = Boton(self.master,
                    text = '00',
                    value = '00',
                    bg = '#171719',
                    fg = '#EAEAEA',
                    font = ('Arial', 20, 'bold')
                    )
    boton00.place(x = 200, y = 500, width = 100, height = 100)