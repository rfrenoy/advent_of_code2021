from typing import Callable, List


def read_puzzle(filepath: str) -> List[int]:
    with open(filepath, 'r') as in_f:
        first_line = in_f.readlines()[0]
        return [int(x) for x in first_line.split(',')]

def fuel_first_star(positions: List[int], target: int) -> int:
    return sum(position_to_target_distance(positions, target))

def position_to_target_distance(positions, target):
    return [abs(x-target) for x in positions]

def fuel_second_star(positions: List[int], target: int) -> int:
    return sum([n*(n+1)/2
            for n in [abs(x-target) for x in positions]])

def best(positions: List[int],
         fuel_rule: Callable[[List[int], int], int]) -> int:
    min_fuel = float('inf')
    res = -1
    for pos in range(min(positions), max(positions)+1):
        used_fuel = fuel_rule(positions, pos)
        if used_fuel < min_fuel:
            min_fuel = used_fuel
            res = pos
    return res, min_fuel


if __name__ == '__main__':
    puzzle = read_puzzle('./inputs/day7.txt')
    print(best(puzzle, fuel_first_star))
    print(best(puzzle, fuel_second_star))