import tkinter as tk
from src.components.App import App

if __name__ == '__main__':
  root = tk.Tk()
  root.title('Calculadora')
  root.geometry('400x600')
  root.resizable(False, False)
  icono = tk.PhotoImage(file = './src/assets/img/icono.png')
  root.iconphoto(True, icono)
  app = App(root)
  root.mainloop()