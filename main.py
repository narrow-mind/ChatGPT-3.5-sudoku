def is_valid(board, row, col, num):
    # Check if the number already exists in the row
    if num in board[row]:
        return False

    # Check if the number already exists in the column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check if the number already exists in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True



def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_board(board):
    for row in board:
        print(row)


# Example Sudoku board (0 represents empty cells, NYT sudoku example)
board = [
    [5, 0, 0, 0, 7, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 2, 0, 5, 0],
    [1, 0, 0, 5, 0, 0, 8, 0, 9],
    [0, 0, 9, 7, 0, 3, 0, 0, 5],
    [2, 0, 4, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 4],
    [9, 3, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 6, 0, 3, 1],
    [0, 0, 0, 0, 0, 0, 9, 0, 0]
]

if solve_sudoku(board):
    print("Solution:")
    print_board(board)
else:
    print("No solution exists.")
