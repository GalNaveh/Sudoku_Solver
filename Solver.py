#Sudoku improved - can solve expert -- using backtracking
import time 

def visual(board):
    for row in range(9):
        if row % 3 == 0 and row != 0:
            print("-"*20)

        for col in range(9):
            if col % 3 == 0 and col != 0:
                print("|", end = "")
            if col == 8:
                print(str(board[row][col]) + " ")
            else:
                print(str(board[row][col]) + " ", end = "")
        
def valid(board,guess,row,col):
    if guess in board[row]:
        return False

    col_num = [board[i][col] for i in range(9)]

    if guess in col_num:
        return False
    
    square_row = (row // 3) * 3
    square_col = (col //3) *3

    block_num = []

    for i in range(square_row,square_row+3):
        for j in range(square_col,square_col+3):
            block_num.append(board[i][j])
    
    if guess in block_num:
        return False
    
    return True

def next_empty(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i , j
    return None,None

def solve(board):

    row, col = next_empty(board)

    if row is None:
        return True

    for guess in range(1,10):

        if valid(board,guess,row,col):

            board[row][col] = guess
        
            if solve(board):
                return True
    
        board[row][col] = 0

    return False

def solved_board(board):
    if solve(board):
        return board



