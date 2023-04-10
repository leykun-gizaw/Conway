import tkinter as tk
from neibors import neibors_tupple

CELLS = 40
MARGIN = 40
SIDE = 20
WIDTH = HEIGHT = 2 * MARGIN + CELLS * SIDE

# ROOT widget #
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT + 40}")

# Current generation #
matrix = [[tk.BooleanVar() for _ in range(CELLS)] for _ in range(CELLS)]

# Frame widget #
frame = tk.Frame(master=root, borderwidth=2)
frame.pack()

# Canvas widget #
canvas = tk.Canvas(master=frame, height=HEIGHT, width=WIDTH, background="grey")
canvas.pack(side=tk.TOP, fill=tk.BOTH)


# Initialize matrix indices #
def initialize(mat):
    for row in range(CELLS):
        for col in range(CELLS):
            mat[row][col].set(True)


def reset():
    initialize(matrix)
    matrix[2][3].set(False)
    matrix[3][3].set(False)
    matrix[3][2].set(False)
    matrix[3][1].set(False)
    matrix[1][2].set(False)

    matrix[38][38].set(False)
    matrix[38][39].set(False)
    matrix[39][38].set(False)
    matrix[39][39].set(False)
    draw(False)


# Draw rectangles with fill color dictated by index values #
def draw(rst=True):
    if rst:
        reset()
    global matrix
    for row in range(CELLS):
        for col in range(CELLS):
            fill = "white" if matrix[row][col].get() else "black"
            outline = "white" if fill == "black" else "black"
            canvas.create_rectangle(
                col * SIDE + MARGIN,
                row * SIDE + MARGIN,
                (col + 1) * SIDE + MARGIN,
                (row + 1) * SIDE + MARGIN,
                fill=fill,
                outline=outline,
            )


# Redraw after rules have been applied #
def play():
    global matrix
    blacks = []
    for row in range(CELLS):
        for col in range(CELLS):
            n = neibors_tupple(matrix, CELLS, row, col)
            if matrix[row][col].get() is True:
                if n.count(False) == 3:
                    blacks.append((row, col))
            else:
                if n.count(False) == 2 or n.count(False) == 3:
                    blacks.append((row, col))
    initialize(matrix)
    for row, col in blacks:
        matrix[row][col].set(False)
    draw(False)
    canvas.after(10, play)


# Initial button draw widget #
btn = tk.Button(frame, text="Draw/Reset", command=draw)
btn.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Redraw button widget #
btn2 = tk.Button(frame, text="Traverse", command=play)
btn2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Main loop of GUI #
root.mainloop()
