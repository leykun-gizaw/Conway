"""Module defines the Canv class"""
import tkinter as tk
from Cell import Cell


class CellsCanvas(tk.Canvas):
    """Class wraps tkinter's Canvas with more functionality"""

    def __init__(
        self, parent: tk.Tk, canvasWidth: int, canvasHeight: int, background: str
    ) -> None:
        """Initialize object with values"""
        super().__init__(parent, width=canvasWidth, height=canvasHeight, bg=background)
        self.__initUI()

    def makeCells(self, width, height, rows, columns):
        """Method creates cells of the given size"""
        self.cells = [
            [
                Cell(self, width, height, posx, posy, tk.BooleanVar())
                for posx in range(columns)
            ]
            for posy in range(rows)
        ]

    def __initUI(self):
        """Draw canvas on screen"""
        self.grid(row=0, column=0)


if __name__ == "__main__":
    parent = tk.Tk()
    canvas = CellsCanvas(parent, 400, 400, "grey")
    canvas.makeCells(40, 40, 8, 8)
    parent.mainloop()
