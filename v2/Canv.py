"""Module defines the Canv class"""
import tkinter as tk
from Cell import Cell


class CellsCanvas(tk.Canvas):
    """Class wraps tkinter's Canvas with more functionality"""

    def __init__(
        self,
        parent: tk.Tk,
        cellSize: int,
        rows: int,
        columns: int,
        background: str,
    ) -> None:
        """Initialize object with values"""
        canvasWidth, canvasHeight = columns * cellSize, rows * cellSize
        super().__init__(parent, width=canvasWidth, height=canvasHeight, bg=background)
        self.__makeCells(cellSize, rows, columns)
        self.__initUI()

    def __makeCells(self, side: int, rows: int, columns: int):
        """Method creates cells of the given size"""
        self.cells = [
            [Cell(self, side, posx, posy, tk.BooleanVar()) for posx in range(columns)]
            for posy in range(rows)
        ]

    def __initUI(self):
        """Draw canvas on screen"""
        self.pack()


if __name__ == "__main__":
    parent = tk.Tk()
    canvas = CellsCanvas(parent, 20, 18, 8, "grey")
    parent.mainloop()
