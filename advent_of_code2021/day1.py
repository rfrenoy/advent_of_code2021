from typing import List, Sequence


def nb_increased_values(in_list: Sequence[int], sequence_length: int) -> int:
    nb_inc = 0
    for i in range(len(in_list)):
        if i-1 >= 0 and i+sequence_length-1 < len(in_list):
            last_three_values = in_list[i-1:i+sequence_length-1]
            current_three_values = in_list[i:i+sequence_length]
            if sum(last_three_values) < sum(current_three_values):
                nb_inc += 1
    return nb_inc


def read_input(filepath: str) -> List[int]:
    with open(filepath, 'r') as in_f:
        return [int(x) for x in in_f.readlines()]


if __name__ == '__main__':
    inputs = read_input('./inputs/day1.txt')
    print(nb_increased_values(inputs, 1))
    print(nb_increased_values(inputs, 3))
