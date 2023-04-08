"""Module defines the Canv class"""
import tkinter as tk


class CellsCanvas(tk.Canvas):
    """Class wraps tkinter's Canvas with more functionality"""

    def __init__(
        self, parent: tk.Tk, canvasWidth: int, canvasHeight: int, background: str
    ) -> None:
        """Initialize object with values"""
        super().__init__(parent, width=canvasWidth, height=canvasHeight, bg=background)
        self.__initUI()

    def __initUI(self):
        """Draw canvas on screen"""
        self.grid(row=0, column=0)


if __name__ == "__main__":
    parent = tk.Tk()
    canvas = CellsCanvas(parent, 400, 400, "grey")
    parent.mainloop()
