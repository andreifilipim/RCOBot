import tkinter as tk
from tkinter import *
import os
from openNavegators import AbrindoRCO
from InteractiveBot import InteractiveBot
import time

classRoom_url = ""

root = tk.Tk()
root.wm_state('zoomed') # Comando para já começar com a janela maximizada
app = InteractiveBot(root)
root.mainloop()