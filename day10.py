import math
from typing import Generator, List, Tuple


def read_puzzle(filepath: str) -> Generator[str, None, None]:
    with open(filepath, 'r', encoding='utf-8') as in_f:
        for read_line in in_f.readlines():
            yield read_line if read_line[-1] != '\n' else read_line[:-1]


def analyse(line_to_analyse: str) -> Tuple[str, List[str]]:
    matching_opening = {')': '(', ']': '[', '>': '<', '}': '{'}
    opening_char_stack = []
    for char in line_to_analyse:
        if char in ['(', '[', '<', '{']:
            opening_char_stack.append(char)
        elif char in [')', ']', '>', '}']:
            opening = opening_char_stack[-1]
            opening_char_stack = opening_char_stack[:-1]
            if opening != matching_opening[char]:
                return char, opening_char_stack
        else:
            raise Exception('Unexpected character')
    return None, opening_char_stack


def completion_score(opening_chars: str) -> int:
    score = 0
    matching_points = {'(': 1, '[': 2, '{': 3, '<': 4}
    for char in opening_chars[::-1]:
        score *= 5
        score += matching_points[char]
    return score


if __name__ == '__main__':
    points_for_error = {')': 3, ']': 57, '}': 1197, '>': 25137}
    puzzle = list(read_puzzle('./inputs/day10.txt'))
    error_score = 0
    compl_scores = []
    for line in puzzle:
        error_char, stack = analyse(line)
        error_score += points_for_error.get(error_char, 0)
        if error_char is None:
            compl_score = completion_score(stack)
            compl_scores.append(compl_score)
    print(error_score)
    compl_scores.sort()
    print(compl_scores[math.floor(len(compl_scores) / 2)])
