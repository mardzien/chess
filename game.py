"""
Chess game
"""
from collections import namedtuple

WHITE = "WHITE"
BLACK = "BLACK"

Field = namedtuple('Field', ['x', 'y'])


class Chessboard(object):

    def __init__(self):
        size = 8
        self.fields = [[self.initialize_field(i, j) for j in range(size)] for i in range(size)]

    @staticmethod
    def initialize_field(x, y):
        return Field(x, y)

    def display(self, piece=" "):

        for j in range(7, -1, -1):
            for i in range(8):
                print(f"[{piece}]", end="")
            print(f" | {j + 1}")
        print("------------------------")
        print("[A][B][C][D][E][F][G][H]")


class Piece(object):

    def __init__(self, color, field):
        self.color = color
        self.field = field
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

