def print_board(board):
    for row in board:
        print(" ".join(str(cell) if cell!=0 else '.' for cell in row))

def is_valid(board,row,col,num):
    for x in range(9):
        if board[row][x]==num:
            return False
    
    for x in range(9):
        if board[x][col]==num:
            return False  
    
    start_row=(row//3)*3
    start_col=(col//3)*3
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col]==num:
                return False
    return True
def find_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j]==0:
                return (i,j)
    return None
def solve_sudoku(board):
    empty=find_empty(board)
    if not empty:
        return True
    row,col=empty
    for num in range(1,10):
        if is_valid(board,row,col,num):
            board[row][col]=num

            if solve_sudoku(board):
                return True
            
            board[row][col]=0
    return False

puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

# Print the initial puzzle
print("Initial Sudoku Puzzle:")
print_board(puzzle)

# Solve the Sudoku puzzle
if solve_sudoku(puzzle):
    print("\nSolved Sudoku Puzzle:")
    print_board(puzzle)
else:
    print("No solution exists for this Sudoku puzzle.")