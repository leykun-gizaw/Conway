"""Main program"""
import tkinter as tk
from Canvas import CellsCanvas
from Cell import Cell

parent = tk.Tk()
canvas = CellsCanvas(parent, 30, "./patterns/0.grid")


def flip():
    newGen = []
    for row in canvas.getCells:
        r = []
        for elem in row:
            v = tk.BooleanVar()
            v.set(not elem.fillVar.get())
            r.append(v)
        newGen.append(r)
    for row in range(len(canvas.getCells)):
        for col in range(len(canvas.getCells[0])):
            canvas.getCells[row][col].fillVar = newGen[row][col]
    canvas.after(10, flip)


tk.Button(parent, text="FLIP", command=flip).pack()

parent.mainloop()
