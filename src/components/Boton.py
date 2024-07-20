import tkinter as tk

class Boton(tk.Button):
  def __init__(self, master, value = None, **kwargs):
    super().__init__(master, **kwargs)
    self.master = master
    self.value = value
    self.config(**kwargs)