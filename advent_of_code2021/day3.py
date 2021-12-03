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

def gamma_rate(diagnostic: List[List[str]]) -> List[str]:
    nb_lines = len(diagnostic)
    res = []
    for column_idx in range(len(diagnostic[0])):
        nb_zeros = sum([line[column_idx] == '0' for line in diagnostic])
        if nb_zeros > nb_lines / 2:
            res.append('0')
        else:
            res.append('1')
    return res

def epsilon_rate(gamma_rate: List[str]) -> List[str]:
    return ['1' if x == '0' else '0'
            for x in gamma_rate]


def rate_to_int(rate: List[str]) -> int:
    return int(''.join(rate), 2)

if __name__ == '__main__':
    diagnostic = read_puzzle('./inputs/day3.txt')
    gamma = gamma_rate(diagnostic)
    epsilon = epsilon_rate(gamma)
    print(rate_to_int(gamma) * rate_to_int(epsilon))
