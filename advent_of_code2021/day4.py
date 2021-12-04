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


def update_boards(draw: int,
                  boards: List[List[List[int]]]) -> List[List[List[int]]]:
    res = []
    for board in boards:
        board = [[x if x != draw else 0 for x in board_line]
                 for board_line in board]
        res.append(board)
    return res


def check_win(board: List[List[int]]):
    # Check lines
    for line in board:
        if sum(line) == 0:
            return True
    # Check column
    for i in range(len(board[0])):
        col = [line[i] for line in board]
        if sum(col) == 0:
            return True
    return False


def winning_puzzle(draws, boards):
    for draw in draws:
        print(draw)
        boards = update_boards(draw, boards)
        for board in boards:
            print(check_win(board))
            if check_win(board):
                return draw, board
    return None, None


if __name__ == '__main__':
    draws, boards = read_puzzle('./inputs/day4.txt')
    last_draw, winning_board = winning_puzzle(draws, boards)
    val = sum([sum(line) for line in winning_board])
    print(last_draw * val)
