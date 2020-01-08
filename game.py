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


if __name__ == "__main__":
    board = Chessboard()
    board.display()