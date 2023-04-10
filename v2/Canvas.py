"""Module defines the Canv class"""
import tkinter as tk
from Cell import Cell
from typing import List


class CellsCanvas(tk.Canvas):
    """Class wraps tkinter's Canvas with more functionality

    The initialized object creates the required cells along with the cells' fill variable.

    Attributes:
        `cells` (private): A 2D matrix consisiting of Pointers to Cell objects
        `side` (private): Size of the Cells. Type of cell is square by default
        `parent` (private): Parent widget that holds this canvas within
        `fillMatrix` (private): A matrix representation of the fill of each cell
        `rows` (private): Number of rows
        `columns` (private): Number of columns
    """

    def __init__(
        self,
        parent: tk.Tk,
        side: int,
        filePath: str,
    ) -> None:
        """Initialize object with values

        Args:
            `parent`: Parent widget this canvas will be nested in
            `side`: Size of the side of the cell square
            `filePath`: Path to the file that contains the grid pattern
        """
        self.__cells = []
        self.__side = side
        self.__parent = parent
        self.__gridMatrix = self.__readMatrix(filePath)
        self.__rows = len(self.__gridMatrix)
        self.__columns = len(self.__gridMatrix[0])
        self.__initUI()

    def __readMatrix(self, filePath: str) -> List[list[bool]]:
        """Method reads a file to construct cells grid

        It opens the grid file and construct a 2D matrix from it.

        Args:
            `filePath`: Path to the file that contains the grid data

        Returns:
            Constructed matrix representation of the grid
        """
        matrix: List[str] = []
        # Read by stripping newline character from file
        with open(filePath, "r") as file:
            line = file.readline()
            while line:
                lastLine = file.readline()
                if lastLine:
                    matrix.append(line[:-1])
                else:
                    matrix.append(line)
                line = lastLine
        return [
            [True if matrix[r][c] == "0" else False for c in range(len(matrix[r]))]
            for r in range(len(matrix))
        ]

    def __neighbours(self, row: int, col: int) -> set[Cell]:
        """Returns a set of neighbours' fill variable for a particular cell

        Args:
            `row`: Row position of current cell
            `col`: Column position of current cell

        Returns:
            Set of neighbours selected from the `cells` matrix
        """
        validIndices = {
            "n": [row - 1, col],
            "s": [row + 1, col],
            "e": [row, col + 1],
            "w": [row, col - 1],
            "ne": [row - 1, col + 1],
            "nw": [row - 1, col - 1],
            "se": [row + 1, col + 1],
            "sw": [row + 1, col - 1],
        }

        neibors = set()
        for _, v in validIndices.items():
            if v[0] >= 0 and v[1] >= 0 and v[0] < self.__rows and v[1] < self.__columns:
                neibors.add(self.__cells[v[0]][v[1]])
        return neibors

    def __makeCells(self) -> None:
        """Create a cells matrix by reading the grid matrix"""
        for posy in range(self.__rows):
            cellsRow = []
            for posx in range(self.__columns):
                fillVar = tk.BooleanVar()
                fillVar.set(self.__gridMatrix[posy][posx])
                cellsRow.append(Cell(self, self.__side, posx, posy, fillVar))
            self.__cells.append(cellsRow)
        for row in range(self.__rows):
            for col in range(self.__columns):
                self.__cells[row][col].neighbours = self.__neighbours(row, col)

    def __initUI(self) -> None:
        """Draw canvas on screen"""
        canvasWidth, canvasHeight = (
            self.__columns * self.__side + 10,
            self.__rows * self.__side + 10,
        )
        super().__init__(
            self.__parent, width=canvasWidth, height=canvasHeight, bg="grey"
        )
        self.__makeCells()
        self.pack()

    @property
    def getCells(self) -> List[list[Cell]]:
        """Return the list of cells"""
        return self.__cells

    @property
    def rows(self):
        """Return number of rows"""
        return self.__rows

    @property
    def columns(self):
        """Return number of columns"""
        return self.__columns
