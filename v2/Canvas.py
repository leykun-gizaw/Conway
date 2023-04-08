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
        self.cells = []
        canvasWidth, canvasHeight = columns * cellSize + 10, rows * cellSize + 10
        super().__init__(parent, width=canvasWidth, height=canvasHeight, bg=background)
        self.__makeCells(cellSize, rows, columns)
        self.__initUI()

    def __makeCells(self, side: int, rows: int, columns: int) -> None:
        """Method creates cells of the given size"""
        for posy in range(rows):
            for posx in range(columns):
                fillVar = tk.BooleanVar()
                fillVar.set(True)
                self.cells.append(Cell(self, side, posx, posy, fillVar))

    def __initUI(self) -> None:
        """Draw canvas on screen"""
        self.pack()


if __name__ == "__main__":
    parent = tk.Tk()
    canvas = CellsCanvas(parent, 30, 20, 20, "grey")
    parent.mainloop()
