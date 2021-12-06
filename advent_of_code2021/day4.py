from typing import List, Tuple


def read_puzzle(filepath: str) -> Tuple[List[int], List[List[List[int]]]]:
    boards = []
    with open(filepath, 'r') as in_f:
        lines = in_f.readlines()
        draws = [int(x) for x in lines[0].split(',')]
        for i in range(2, len(lines) - 4, 6):
            board = [[int(x) for x in lines[j].split(' ') if x != '']
                     for j in range(i, i + 5)]
            boards.append(board)
    return draws, boards


def update_masks(draw: int,
                 boards: List[List[List[int]]],
                 masks: List[List[List[int]]]) -> List[List[List[int]]]:
    res = []
    for i, board in enumerate(boards):
        mask = [[masks[i][j][k] if x != draw else 1 
                 for k, x in enumerate(board_line)]
                 for j, board_line in enumerate(board)]
        res.append(mask)
    return res


def check_win(mask: List[List[int]]):
    # Check lines
    for line in mask:
        if sum(line) == 5:
            return True
    # Check column
    for i in range(len(mask[0])):
        col = [line[i] for line in mask]
        if sum(col) == 5:
            return True
    return False


def first_winning_puzzle(draws, boards):
    masks = create_masks(boards)
    for draw in draws:
        masks = update_masks(draw, boards, masks)
        for i, mask in enumerate(masks):
            if check_win(mask):
                return draw, boards[i], mask
    return None, None


def last_winning_puzzle(draws, boards):
    winning_boards = []
    remaining_boards = list(boards)
    masks = create_masks(boards)
    remaining_masks = list(masks)
    for draw in draws:
        remaining_masks = update_masks(draw, remaining_boards, remaining_masks)
        i = 0
        while i < len(remaining_masks):
            mask = remaining_masks[i]
            if check_win(mask):
                winning_boards.append((draw, remaining_boards[i], mask))
                remaining_boards = remaining_boards[:i] + remaining_boards[i +
                                                                           1:]

                remaining_masks = remaining_masks[:i] + remaining_masks[i +
                                                                           1:]
            if len(remaining_boards) == 0:
                return winning_boards[-1]
            i += 1
    return winning_boards[-1]


def create_masks(boards):
    return [[[0 for _ in board_line] 
             for board_line in board]
                for board in boards]

def sum_remaining_values(board, mask):
    res = 0
    for i, board_line in enumerate(board):
        for j, elt in enumerate(board_line):
            if mask[i][j] == 0:
                res += elt
    return res


if __name__ == '__main__':
    draws, boards = read_puzzle('./inputs/day4.txt')

    last_draw, winning_board, mask = first_winning_puzzle(draws, boards)
    val = sum_remaining_values(winning_board, mask)
    print(last_draw * val)

    last_draw, last_winning_board, mask = last_winning_puzzle(draws, boards)
    val = sum_remaining_values(last_winning_board, mask)
    print(last_draw * val)
