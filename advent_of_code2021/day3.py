from typing import List


def read_puzzle(filepath: str) -> List[List[str]]:
    res = []
    with open(filepath, 'r') as in_f:
        for line in in_f.readlines():
            new_line = []
            for ch in line[:-1]:
                new_line.append(ch)
            res.append(new_line)
    return res


def column(in_list: List[List], idx: int) -> List:
    return [line[idx] for line in in_list]


def most_common_value(in_list: List[str], equal_decision: str) -> str:
    nb_zeros = sum([elt == '0' for elt in in_list])
    lst_size = len(in_list)
    if nb_zeros > lst_size / 2:
        return '0'
    if nb_zeros < lst_size / 2:
        return '1'
    return equal_decision


def least_common_value(in_list: List[str], equal_decision: str) -> str:
    nb_zeros = sum([elt == '0' for elt in in_list])
    lst_size = len(in_list)
    if nb_zeros > lst_size / 2:
        return '1'
    if nb_zeros < lst_size / 2:
        return '0'
    return equal_decision


def gamma_rate(diagnostic: List[List[str]]) -> List[str]:
    nb_lines = len(diagnostic)
    res = []
    for column_idx in range(len(diagnostic[0])):
        res.append(most_common_value(column(diagnostic, column_idx), '1'))
    return res


def oxygen_rate(diagnostic: List[List[str]]) -> int:
    remaining = list(diagnostic)
    bit_idx = 0
    while len(remaining) > 1:
        curr_col = column(remaining, bit_idx)
        most_common = most_common_value(curr_col, '1')
        remaining = [
            line for line in remaining if line[bit_idx] == most_common
        ]
        bit_idx += 1
    return int(''.join(remaining[0]), 2)


def co2_rate(diagnostic: List[List[str]]) -> int:
    remaining = list(diagnostic)
    bit_idx = 0
    while len(remaining) > 1:
        curr_col = column(remaining, bit_idx)
        most_common = least_common_value(curr_col, '0')
        remaining = [
            line for line in remaining if line[bit_idx] == most_common
        ]
        bit_idx += 1
    return int(''.join(remaining[0]), 2)


def epsilon_rate(gamma_rate: List[str]) -> List[str]:
    return ['1' if x == '0' else '0' for x in gamma_rate]


def rate_to_int(rate: List[str]) -> int:
    return int(''.join(rate), 2)


if __name__ == '__main__':
    diagnostic = read_puzzle('./inputs/day3.txt')
    gamma = gamma_rate(diagnostic)
    epsilon = epsilon_rate(gamma)
    print(rate_to_int(gamma) * rate_to_int(epsilon))
    print(oxygen_rate(diagnostic) * co2_rate(diagnostic))
