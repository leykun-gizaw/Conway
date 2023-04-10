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
        self.__setFill(fillVar)
        self.__setOutline()
        self.__fillVar = fillVar
        self.__canvas = canvas
        self.__cell = canvas.create_rectangle(
            posx * side + 6,
            posy * side + 6,
            (posx + 1) * side + 6,
            (posy + 1) * side + 6,
            fill=self.__fill,
            outline=self.__outline,
        )

    @property
    def fillVar(self):
        """Returns the fill variable of current cell"""
        return self.__fillVar

    @fillVar.setter
    def fillVar(self, fillVar: tk.BooleanVar) -> None:
        """Updates the cell's fill value

        Args:
            `fillVar`: Variable representing what the fill should be

        Returns:
            None
        """

        self.__setFill(fillVar)
        self.__setOutline()
        self.__fillVar = fillVar
        self.__canvas.itemconfig(self.__cell, fill=self.__fill, outline=self.__outline)

    @property
    def neighbours(self) -> set:
        """Return the set of neighbours constructed"""
        return self.__neighbours

    @neighbours.setter
    def neighbours(self, neighbours: set) -> None:
        self.__neighbours = neighbours

    def __setFill(self, fillVar: tk.BooleanVar) -> None:
        """Method configures fill value according to passed boolean variable

        Args:
            `fillVar`: Variable representing what the fill should be

        Returns:
            None
        """
        self.__fill = "white" if fillVar.get() == True else "black"

    def __setOutline(self) -> None:
        """Method configures fill value according to passed boolean variable"""
        self.__outline = "white" if self.__fill == "black" else "black"
