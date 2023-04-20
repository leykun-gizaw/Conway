"""Main program"""
import tkinter as tk
from Canvas import CellsCanvas
from Cell import Cell
from time import sleep

parent = tk.Tk()
gridFrame = tk.Frame(parent, padx=10, pady=10, relief=tk.RAISED, background="white")
canvas = CellsCanvas(gridFrame, side=20, filePath="./patterns/gosper_gun.csv")
gridFrame.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
stop = False


def flip():
    newGen = []
    for row in canvas.getCells:
        r = []
        for elem in row:
            v = tk.BooleanVar()
            v.set(True)
            offFills = 0
            onFills = 0
            for neighbour in elem.neighbours:
                if neighbour.fillVar.get() == False:
                    offFills += 1
                else:
                    onFills += 1
            if elem.fillVar.get() == True:
                if offFills == 3:
                    v.set(False)
            elif offFills == 3 or offFills == 2:
                v.set(False)
            r.append(v)
        newGen.append(r)
    for row in range(len(canvas.getCells)):
        for col in range(len(canvas.getCells[0])):
            canvas.getCells[row][col].fillVar = newGen[row][col]
    if not stop:
        canvas.after(1, flip)


def changeStop(val: bool) -> None:
    global stop
    stop = val
    if not stop:
        flip()


controlsFrame = tk.Frame(parent, padx=10, pady=10, relief=tk.RAISED)
tk.Button(controlsFrame, text="START/NEXT", command=flip).pack(side=tk.LEFT, expand=True)
tk.Button(controlsFrame, text="CONTINUE", command=lambda: changeStop(False)).pack(
    side=tk.LEFT, expand=True
)
tk.Button(controlsFrame, text="STOP", command=lambda: changeStop(True)).pack(
    side=tk.LEFT, expand=True
)
controlsFrame.pack(side=tk.RIGHT)

parent.mainloop()
