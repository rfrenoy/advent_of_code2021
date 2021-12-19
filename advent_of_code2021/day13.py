import numpy as np
from dataclasses import dataclass


@dataclass
class Fold:
    axis: str
    value: int


def read_puzzle(filepath: str) -> tuple[list[list[int]], list[Fold]]:
    with open(filepath, 'r', encoding='utf-8') as in_f:
        lines = in_f.readlines()

    res = []
    folds_list = []
    for line in lines:
        if line[0] not in ['\n', 'f']:
            res.append([int(x) for x in line.split(',')])
        elif 'fold' in line:
            axis = line.split('=')[0][-1]
            val = int(line.split('=')[1])
            folds_list.append(Fold(axis, val))
    return res, folds_list


def create_dot_matrix(dots_list: list[list[int]]) -> np.ndarray:
    zipped = list(zip(*dots_list))
    width = max(zipped[0]) + 1
    height = max(zipped[1]) + 1
    res = np.zeros((height, width))
    for dot in dots_list:
        res[dot[1], dot[0]] = 1
    return res


def fold_mat(mat: np.ndarray, fold: Fold) -> np.ndarray:
    if fold.axis == 'x':
        res = np.zeros((mat.shape[0], fold.value))
        res[:, :fold.value] = mat[:, :fold.value]
        for i in range(mat.shape[0]):
            for j in range(fold.value):
                res[i, j] += mat[i, mat.shape[1] - j - 1]
    else:
        res = np.zeros((fold.value, mat.shape[1]))
        res[:fold.value, :] = mat[:fold.value, :]
        for i in range(fold.value):
            for j in range(mat.shape[1]):
                res[i, j] += mat[mat.shape[0] - i - 1, j]
    return res


def overlapping_strategy(mat: np.ndarray) -> np.ndarray:
    return np.where(mat > 0, 1, 0)


if __name__ == '__main__':
    dots, folds = read_puzzle('./inputs/day13.txt')
    matr = create_dot_matrix(dots)
    for folding_iteration, current_fold in enumerate(folds):
        matr = overlapping_strategy(fold_mat(matr, current_fold))
        if folding_iteration == 0:
            print(f'Solution first star: {matr.sum()}')
    print(f'Solution second star: {matr}')