"""Main program"""
import tkinter as tk
from Canvas import CellsCanvas
from Cell import Cell

parent = tk.Tk()
frame = tk.Frame(parent, padx=10, pady=10, relief=tk.SUNKEN)
canvas = CellsCanvas(frame, side=20, filePath="./patterns/glider.csv")
frame.pack()


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
    canvas.after(10, flip)


flip()

# tk.Button(parent, text="FLIP", command=flip).pack()

parent.mainloop()
