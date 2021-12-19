import numpy as np
from advent_of_code2021.day13 import fold_mat, Fold


def test_fold_mat_should_fold_fold_vertically_on_given_column_and_sum_overlapping_values():
    # Given
    before_fold = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
    after_fold = np.array([[6, 6], [16, 16]])
    fold = Fold('x', 2)

    # When
    folded = fold_mat(before_fold, fold)

    # Then
    np.testing.assert_array_equal(folded, after_fold)
