from typing import List
import numpy as np


def read_puzzle(filepath: str) -> List[List[int]]:
    mat = []
    with open(filepath, 'r', encoding='utf-8') as in_f:
        for line in in_f.readlines():
            mat.append([int(x) for x in line if x != '\n'])
    return mat


def who_flashes(mat):
    return np.argwhere(np.array(mat) > 9)


def neighboors(mat, i, j):
    lines = range(max([0, i - 1]), min([np.array(mat).shape[0], i + 2]))
    cols = range(max([0, j - 1]), min([np.array(mat).shape[1], j + 2]))
    return [(m, n) for m in lines for n in cols if not ((m == i) and (n == j))]


def step(mat):
    mat = mat + 1
    has_flashed = np.zeros(mat.shape)
    nb_flashes = 0
    while True:
        flashes = who_flashes(mat)
        if len(flashes) == 0:
            return mat, nb_flashes
        for i, j in flashes:
            mat[i][j] = 0
            if has_flashed[i][j] == 0:
                has_flashed[i][j] = 1
                nb_flashes += 1
                for ni, nj in neighboors(mat, i, j):
                    if not has_flashed[ni, nj]:
                        mat[ni, nj] += 1


if __name__ == '__main__':
    puzzle = np.array(read_puzzle('./inputs/day11.txt'))
    total_flashes = 0
    for s in range(100):
        puzzle, flashes = step(puzzle)
        total_flashes += flashes
    print(total_flashes)

    puzzle = np.array(read_puzzle('./inputs/day11.txt'))
    step_idx = 0
    while True:
        puzzle, flashes = step(puzzle)
        step_idx += 1
        if puzzle.sum().sum() == 0:
            break
    print(step_idx)
    