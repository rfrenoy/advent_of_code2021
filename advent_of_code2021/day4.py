from __future__ import annotations
from typing import List, Tuple


class Game:
    def __init__(self):
        self.boards = []
        self.draws = []

    @classmethod
    def read_puzzle(cls, filepath: str) -> Game:
        game = Game()
        with open(filepath, 'r') as in_f:
            lines = in_f.readlines()
            game.draws = [int(x) for x in lines[0].split(',')]
            for i in range(2, len(lines) - 4, 6):
                board = Board(
                    [[int(x) for x in lines[j].split(' ') if x != '']
                     for j in range(i, i + 5)])
                game.boards.append(board)
        return game

    def first_winning_puzzle(self) -> Tuple[int, Board]:
        for draw in self.draws:
            for board in self.boards:
                board.update_mask(draw)
                if board.win():
                    return draw, board
        raise Exception('No winning puzzle')

    def last_winning_puzzle(self) -> Tuple[int, Board]:
        winning_boards = []
        remaining_boards = list(self.boards)
        for draw in self.draws:
            i = 0
            while i < len(remaining_boards):
                board = remaining_boards[i]
                board.update_mask(draw)
                if board.win():
                    winning_boards.append((draw, board))
                    remaining_boards = remaining_boards[:i] + remaining_boards[
                        i + 1:]
                else:
                    i += 1

                if len(remaining_boards) == 0:
                    return winning_boards[-1]

        if len(winning_boards) > 0:
            return winning_boards[-1]

        raise Exception('No winning puzzle')

    def reset(self):
        for board in self.boards:
            board.reset_mask()


class Board:
    def __init__(self, vals):
        self._values = vals
        self.reset_mask()

    @property
    def mask(self) -> List[List[int]]:
        return self._mask

    def reset_mask(self):
        self._mask = [[0 for _ in board_line] for board_line in self._values]

    def win(self) -> bool:
        # Check lines
        for line in self._mask:
            if sum(line) == 5:
                return True
        # Check column
        for i in range(len(self._mask[0])):
            col = [line[i] for line in self._mask]
            if sum(col) == 5:
                return True
        return False

    def update_mask(self, draw):
        self._mask = [[
            self.mask[j][k] if x != draw else 1
            for k, x in enumerate(board_line)
        ] for j, board_line in enumerate(self._values)]

    def sum_remaining_values(self) -> int:
        res = 0
        for i, board_line in enumerate(self._values):
            for j, elt in enumerate(board_line):
                if self._mask[i][j] == 0:
                    res += elt
        return res


if __name__ == '__main__':
    game = Game.read_puzzle('./inputs/day4.txt')

    last_draw, winning_board = game.first_winning_puzzle()
    val = winning_board.sum_remaining_values()
    print(last_draw * val)

    game.reset()
    last_draw, last_winning_board = game.last_winning_puzzle()
    val = last_winning_board.sum_remaining_values()
    print(last_draw * val)
