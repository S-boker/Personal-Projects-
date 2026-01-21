# sudoku_solver.py
# Made by ChatGPT
GRID_SIZE = 9
BOX_SIZE = 3
EMPTY = 0

def create_empty_board():
    return [[EMPTY for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def print_board(board):
    print("-" * 21)
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            print(board[r][c], end=" ")
        print()
    print("-" * 21)

def is_valid_row(row):
    nums = [n for n in row if n != EMPTY]
    return len(nums) == len(set(nums))

def read_board_from_input():
    board = create_empty_board()
    print("Enter 9 rows (use 0 for blanks)")
    for r in range(GRID_SIZE):
        while True:
            row_input = input(f"row {r + 1}: ")
            if len(row_input) != GRID_SIZE:
                continue
            try:
                values = [int(ch) for ch in row_input]
            except ValueError:
                continue
            if not is_valid_row(values):
                continue
            board[r] = values
            break
    return board

def is_valid_move(board, row, col, value):
    if value in board[row]:
        return False
    for r in range(GRID_SIZE):
        if board[r][col] == value:
            return False
    box_row = (row // BOX_SIZE) * BOX_SIZE
    box_col = (col // BOX_SIZE) * BOX_SIZE
    for r in range(box_row, box_row + BOX_SIZE):
        for c in range(box_col, box_col + BOX_SIZE):
            if board[r][c] == value:
                return False
    return True

def find_empty_cell(board):
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if board[r][c] == EMPTY:
                return r, c
    return None

def solve(board):
    empty = find_empty_cell(board)
    if not empty:
        return True
    row, col = empty
    for value in range(1, GRID_SIZE + 1):
        if is_valid_move(board, row, col, value):
            board[row][col] = value
            if solve(board):
                return True
            board[row][col] = EMPTY
    return False

def main():
    board = read_board_from_input()
    if solve(board):
        print_board(board)
    else:
        print("Unsolvable")

if __name__ == "__main__":
    main()
