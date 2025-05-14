import tkinter as tk
import game

uiwidth = 50

m = tk.Tk()

m.title("Pong!")


ballSpeed = tk.Scale(m, from_=100, to=1000, orient=HORIZONTAL)
playerSpeed = tk.Scale(m, from_=400, to=1000, orient=HORIZONTAL)

playBtn = tk.Button(m, width=uiwidth, text="run", command=game.pygamerun)
