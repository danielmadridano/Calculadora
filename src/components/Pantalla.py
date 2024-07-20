import tkinter as tk

class Pantalla(tk.Entry):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
    self.expresion = ''
    self.resultado = ''
    self.entryExpresion = tk.Entry(master,
                                   bg = '#000000',
                                   fg = '#FFFFFF',
                                   font = ('Arial', 20, 'bold'),
                                   border = 0,
                                   justify = tk.RIGHT
                                   )
    self.entryExpresion.place(x = 0, y = 0, width = 400, height = 50)
    self.entryResultado = tk.Entry(master,
                                   bg = '#000000',
                                   fg = '#FFFFFF',
                                   font = ('Arial', 20, 'bold'),
                                   border = 0,
                                   justify = tk.RIGHT
                                   )
    self.entryResultado.place(x = 0, y = 50, width = 400, height = 50)
    
  def limpiar(self):
    self.entryExpresion.delete(0, tk.END)
    self.entryResultado.delete(0, tk.END)
    self.expresion = ''
    self.resultado = ''
    
  def pulsarTecla(self, tecla):
    if self.entryResultado.get() == '':
      n = len(self.entryExpresion.get())   
      self.entryExpresion.insert(n, tecla)
      self.expresion += tecla
    elif self.entryResultado.get() == 'Syntax Error' or self.entryResultado.get() == 'Math Error':
      pass
    else:
      if tecla.isdigit():
        self.limpiar()
        self.entryExpresion.insert(0, tecla)
        self.expresion += tecla
      else:
        self.entryExpresion.insert(0, self.resultado)
        self.entryResultado.delete(0, tk.END)
        n = len(self.entryExpresion.get())
        self.entryExpresion.insert(n, tecla)
        self.expresion += tecla
      
  def evaluarExpresion(self):
    try:
      self.resultado = eval(self.expresion)
      if self.resultado % 1 == 0: 
        self.resultado = format(self.resultado, '.0f')
        self.resultado = str(self.resultado)
      else:
        self.resultado = str(self.resultado)
      self.entryExpresion.delete(0, tk.END)
      self.entryResultado.delete(0, tk.END)
      self.entryResultado.insert(0, self.resultado)
      self.expresion = self.resultado
    except SyntaxError:
      self.entryExpresion.delete(0, tk.END)
      self.entryResultado.delete(0, tk.END)
      self.entryResultado.insert(0, 'Syntax Error')
      self.expresion = self.resultado
      self.resultado = ''
    except ZeroDivisionError:
      self.entryExpresion.delete(0, tk.END)
      self.entryResultado.delete(0, tk.END)
      self.entryResultado.insert(0, 'Math Error')
      self.expresion = self.resultado
      self.resultado = ''
  
  def retroceso(self):
    self.expresion = self.expresion[:-1]
    self.entryExpresion.delete(0, tk.END)
    self.entryExpresion.insert(0, self.expresion)