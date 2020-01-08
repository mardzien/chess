"""
Chess game
"""
from collections import namedtuple
import pprint

WHITE = "WHITE"
BLACK = "BLACK"

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
        self.graphic_representation = None

    def display(self):
        if self.graphic_representation is None:
            raise Exception("Invalid graphic representation.")
        else:
            print(self.graphic_representation)


class Pawn(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == BLACK:
            self.graphic_representation = "♙"
        elif color == WHITE:
            self.graphic_representation = "♟"
        else:
            raise Exception("Invalid piece color.")


class Rook(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == BLACK:
            self.graphic_representation = "♖"
        elif color == WHITE:
            self.graphic_representation = "♜"
        else:
            raise Exception("Invalid piece color.")


class Bishop(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == BLACK:
            self.graphic_representation = "♗"
        elif color == WHITE:
            self.graphic_representation = "♝"
        else:
            raise Exception("Invalid piece color.")


class Knight(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == BLACK:
            self.graphic_representation = "♘"
        elif color == WHITE:
            self.graphic_representation = "♞"
        else:
            raise Exception("Invalid piece color.")


class King(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == BLACK:
            self.graphic_representation = "♔"
        elif color == WHITE:
            self.graphic_representation = "♚"
        else:
            raise Exception("Invalid piece color.")


class Queen(Piece):

    def __init__(self, color):
        super().__init__(color)
        if color == BLACK:
            self.graphic_representation = "♕"
        elif color == WHITE:
            self.graphic_representation = "♛"
        else:
            raise Exception("Invalid piece color.")


if __name__ == "__main__":
    print("Chessboard: ")
    board = Chessboard()
    board.display()

    piece_types = [Pawn, Knight, Bishop, Rook, Queen, King]
    white_pieces = [t(color=WHITE) for t in piece_types]
    black_pieces = [t(color=BLACK) for t in piece_types]

    print("White pieces:")
    for piece in white_pieces:
        piece.display()

    print("Black pieces:")
    for piece in black_pieces:
        piece.display()
