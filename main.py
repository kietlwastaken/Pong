import tkinter as tk
import game

running = True

uiwidth = 50

m = tk.Tk()

m.title("Pong!")

def run():
    m.withdraw()
    game.pygamerun(playerSpeed.get(), ballSpeed.get())
    m.deiconify()

ballSpeed = tk.Scale(m, from_=100, to=1000, orient="horizontal")
playerSpeed = tk.Scale(m, from_=400, to=1000, orient="horizontal")

playBtn = tk.Button(m, width=uiwidth, text="play!", command=run)

uiElements = [
    ballSpeed,
    playerSpeed,
    playBtn
]

for element in uiElements:
    element.pack()


tk.mainloop()