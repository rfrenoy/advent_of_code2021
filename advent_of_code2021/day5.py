import re
import numpy as np
from typing import Generator, Iterable, Tuple


def read_puzzle(filepath: str) -> Generator[Iterable[int], None, None]:
    with open(filepath, 'r') as in_f:
        for line in in_f.readlines():
            indices = re.split(r'^([0-9]*),([0-9]*) -> ([0-9]*),([0-9]*)$',
                               line)[1:-1]
            yield [int(x) for x in indices]


def matrix_size(puzzle: Iterable[Iterable[int]]) -> Tuple[int, int]:
    zipped = list(zip(*puzzle))
    return (max(zipped[0] + zipped[2]) + 1, max(zipped[1] + zipped[3]) + 1)


def start_end_step(a, b):
    if a <= b:
        return a, b + 1, 1
    return a, b - 1, -1


def draw_line(m, n, consider_diagonal, x1, y1, x2, y2):
    new_line_matrix = np.zeros((m, n))
    x_start, x_end, x_step = start_end_step(x1, x2)
    y_start, y_end, y_step = start_end_step(y1, y2)
    if x1 == x2:
        for i in range(y_start, y_end, y_step):
            new_line_matrix[x1, i] = 1

    elif y1 == y2:
        for i in range(x_start, x_end, x_step):
            new_line_matrix[i, y1] = 1
    else:
        if consider_diagonal:
            i = x_start
            j = y_start
            while True:
                if i == x_end:
                    break
                new_line_matrix[i][j] = 1
                i += x_step
                j += y_step
    return new_line_matrix


if __name__ == '__main__':
    puzzle = list(read_puzzle('./inputs/day5.txt'))
    lines, columns = matrix_size(puzzle)

    matrix = np.zeros((lines, columns))
    for idx in puzzle:
        matrix = matrix + draw_line(lines, columns, False, *idx)
    print(np.sum(matrix >= 2))

    matrix = np.zeros((lines, columns))
    for idx in puzzle:
        matrix = matrix + draw_line(lines, columns, True, *idx)
    print(np.sum(matrix >= 2))
