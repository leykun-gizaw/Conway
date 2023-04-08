"""Module defines Cell class"""
import tkinter as tk


class Cell:
    """Cell represents a cell in a canvas"""

    def __init__(
        self,
        canvas: tk.Canvas,
        side: int,
        posx: int,
        posy: int,
        fillVar: tk.BooleanVar,
    ):
        """Initialze object with values"""
        self.fill = "white" if fillVar.get() == True else "black"
        self.outline = "white" if fillVar.get() == False else "black"
        canvas.create_rectangle(
            posx * side,
            posy * side,
            (posx + 1) * side,
            (posy + 1) * side,
            fill=self.fill,
            outline=self.outline,
        )
