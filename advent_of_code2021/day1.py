from typing import List, Sequence


def nb_increased_values(in_list: Sequence[int]) -> int:
    nb_inc = 0
    for i, elt in enumerate(in_list):
        if i-1 >= 0:
            if elt > in_list[i-1]:
                print(f'{elt}>{in_list[i-1]}')
                nb_inc += 1
            else:
                print(f'{elt}<={in_list[i-1]}')
                
    return nb_inc

def read_input(filepath: str) -> List[int]:
    with open(filepath, 'r') as in_f:
        return [int(x) for x in in_f.readlines()]

if __name__ == '__main__':
    inputs = read_input('../inputs/day1.txt')
    print(nb_increased_values(inputs))
