import numpy as np
import functools


def read_puzzle(filepath):
    with open(filepath, 'r') as in_f:
        lines = in_f.readlines()
    return np.array([[int(x) for x in line if x != '\n'] for line in lines])


def neighboors_coordinates(mat, interest_point):
    i, j = interest_point
    n_coordinates = []
    if i >= 1:
        n_coordinates.append((i - 1, j))
    if j >= 1:
        n_coordinates.append((i, j - 1))
    if i < mat.shape[0] - 1:
        n_coordinates.append((i + 1, j))
    if j < mat.shape[1] - 1:
        n_coordinates.append((i, j + 1))
    return n_coordinates


def neighboors_values(mat, interest_point):
    return [mat[n] for n in neighboors_coordinates(mat, interest_point)]


def lower_points(mat):
    low_points_mask = np.zeros(mat.shape)
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            n = neighboors_values(mat, (i, j))
            if mat[i][j] < min(n):
                low_points_mask[i][j] = 1
    return low_points_mask


def basin_size(mat, low_point, markers):
    i, j = low_point
    if mat[i][j] == 9:
        return
    markers[i][j] = 1
    neighboor_markers = neighboors_values(markers, (i, j))
    neighboor_mat = neighboors_values(mat, (i, j))
    if sum(neighboor_markers) + sum(
        [1 if x == 9 else 0 for x in neighboor_mat]) == len(neighboor_markers):
        return

    nidx = neighboors_coordinates(mat, (i, j))
    for n in nidx:
        if (mat[n] != 9) and (markers[n] != 1):
            basin_size(mat, n, markers)
    return np.nonzero(markers)[0].shape[0]


if __name__ == '__main__':
    puzzle = read_puzzle('./inputs/day9.txt')
    print(puzzle)
    lp = lower_points(puzzle)
    print((lp + np.multiply(lp, puzzle)).sum().sum())
    basin_sizes = []
    for low_point in list(zip(*np.nonzero(lp))):
        a = basin_size(puzzle, low_point, np.zeros(puzzle.shape))
        basin_sizes.append(a)
    basin_sizes.sort()
    print(functools.reduce(lambda a, b: a * b, basin_sizes[-3:]))
