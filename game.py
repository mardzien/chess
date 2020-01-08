"""
Chess game
"""
from collections import namedtuple
import pprint

pp = pprint.PrettyPrinter(indent=4)

Field = namedtuple('Field', ['x', 'y'])


class Chessboard(object):

    def __init__(self):
        size = 8
        self.fields = [[self.initialize_field(i, j) for j in range(size)] for i in range(size)]

    @staticmethod
    def initialize_field(x, y):
        return Field(x, y)

    def display(self):
        pp.pprint(self.fields)


class Piece(object):

    def __init__(self, color):
        self.color = color


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "WHITE":
            self.graphic_representation = "♙"
        elif color == "BLACK":
            self.graphic_representation = "♟"
        else:
            raise Exception("Invalid piece color.")


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "WHITE":
            self.graphic_representation = "♖"
        elif color == "BLACK":
            self.graphic_representation = "♜"
        else:
            raise Exception("Invalid piece color.")


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "WHITE":
            self.graphic_representation = "♗"
        elif color == "BLACK":
            self.graphic_representation = "♝"
        else:
            raise Exception("Invalid piece color.")


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "WHITE":
            self.graphic_representation = "♘"
        elif color == "BLACK":
            self.graphic_representation = "♞"
        else:
            raise Exception("Invalid piece color.")


class King(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "WHITE":
            self.graphic_representation = "♔"
        elif color == "BLACK":
            self.graphic_representation = "♚"
        else:
            raise Exception("Invalid piece color.")


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == "WHITE":
            self.graphic_representation = "♕"
        elif color == "BLACK":
            self.graphic_representation = "♛"
        else:
            raise Exception("Invalid piece color.")


if __name__ == "__main__":
    board = Chessboard()
    board.display()


