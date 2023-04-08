"""Module defines Cell class"""
import tkinter as tk


class Cell:
    """Cell represents a cell in a canvas"""

    def __init__(
        self,
        canvas: tk.Canvas,
        width: int,
        height: int,
        posx: int,
        posy: int,
        fillVar: tk.BooleanVar,
    ):
        """Initialze object with values"""
        canvas.create_rectangle(posx * 40, posy * 40, (posx + 1) * 40, (posy + 1) * 40)
