# sudoku_solver_csp.py 
# Made by ChatGPT
from typing import List, Optional, Tuple

Board = List[List[int]]

GRID_SIZE = 9
BOX_SIZE = 3
EMPTY = 0
DIGITS = range(1, 10)

def used_in_row(board: Board, row: int, value: int) -> bool:
    return value in board[row]

def used_in_col(board: Board, col: int, value: int) -> bool:
    return any(board[r][col] == value for r in range(GRID_SIZE))

def used_in_box(board: Board, row: int, col: int, value: int) -> bool:
    box_row = (row // BOX_SIZE) * BOX_SIZE
    box_col = (col // BOX_SIZE) * BOX_SIZE
    return any(
        board[r][c] == value
        for r in range(box_row, box_row + BOX_SIZE)
        for c in range(box_col, box_col + BOX_SIZE)
    )

def is_safe(board: Board, row: int, col: int, value: int) -> bool:
    return (
        not used_in_row(board, row, value)
        and not used_in_col(board, col, value)
        and not used_in_box(board, row, col, value)
    )

def find_empty(board: Board) -> Optional[Tuple[int, int]]:
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == EMPTY:
                return r, c
    return None

def solve(board: Board) -> bool:
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    for value in DIGITS:
        if is_safe(board, row, col, value):
            board[row][col] = value
            if solve(board):
                return True
            board[row][col] = EMPTY
    return False

def print_board(board: Board) -> None:
    for r in range(GRID_SIZE):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(GRID_SIZE):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            print(board[r][c], end=" ")
        print()

if __name__ == "__main__":
    puzzle = [
        [5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,4,1,9,0,0,5],
        [0,0,0,0,8,0,0,7,9],
    ]
    solve(puzzle)
    print_board(puzzle)
