from enum import Enum
from typing import List

class Direction(Enum):
    UP = 1
    DOWN = 2
    FORWARD = 3

    @classmethod
    def from_input(cls, in_str: str):
        mapping = {'forward': Direction.FORWARD,
                   'up': Direction.UP,
                   'down': Direction.DOWN}
        return mapping[in_str]

class Submarine():
    def __init__(self):
        self._horizontal_pos = 0
        self._depth = 0

    def move_down(self, val: int):
        self._depth += val

    def move_forward(self, val: int):
        self._horizontal_pos += val

    def __repr__(self):
        return f'x={self._horizontal_pos}\ty={self._depth}'

    def move(self, direction: Direction, val: int):
        if direction == Direction.UP:
            self.move_down(-val)
        elif direction == Direction.DOWN:
            self.move_down(val)
        elif direction == Direction.FORWARD:
            self.move_forward(val)
        else:
            raise Exception('Wrong input')

    def multiply_pos(self):
        return self._horizontal_pos * self._depth

def read_puzzle_input(filepath: str):
    """
    toto
    """

    res = []
    with open(filepath, 'r') as in_f:
        for l in in_f.readlines():
            splitted_line = l.split(' ')
            res.append((Direction.from_input(splitted_line[0]), 
                        int(splitted_line[1])))
    return res


if __name__ == '__main__':
    submarine = Submarine()
    moves = read_puzzle_input('./inputs/day2.txt')
    for move in moves:
        submarine.move(*move)
    print(submarine)
    print(submarine.multiply_pos())
