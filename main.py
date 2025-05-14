import tkinter as tk
import game

uiwidth = 50

m = tk.Tk()

m.title("Pong!")

def run():
    m.withdraw()
    while running:
        game.pygamerun(playerSpeed.get(), ballSpeed.get())
    m.deiconify()

ballSpeed = tk.Scale(m, from_=100, to=1000, orient=HORIZONTAL)
playerSpeed = tk.Scale(m, from_=400, to=1000, orient=HORIZONTAL)

playBtn = tk.Button(m, width=uiwidth, text="play!", command=run)

m.pack(
    ballSpeed,
    playerSpeed,
    playBtn
)

tk.mainloop()