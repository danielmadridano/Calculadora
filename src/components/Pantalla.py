import tkinter as tk

class Pantalla(tk.Entry):
  def __init__(self, master, **kwargs):
    super().__init__(master, **kwargs)
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