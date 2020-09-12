def find_empty_cell(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == '.':
                return (i,j)
    return None
            
def possible_values(p, board):
    i,j = p
    row_set = set([board[i][c] for c in range(9) if board[i][c] != '.'])
    col_set = set([board[r][j] for r in range(9) if board[r][j] != '.'])
    b_i, b_j = i//3, j//3
    subbox_set = set([board[b_i*3 + r][b_j*3 + c] for r in range(3) for c in range(3) if board[b_i*3 + r][b_j*3 + c] != '.'])
    allowed_set = set([str(k) for k in range(1,10)])
    
    return list(allowed_set.difference(row_set.union(col_set).union(subbox_set)))

def backtrack(board):
    # if there are no more cells to fill then return True
    # find an empty cell
    # figure out the possible numbers for it
    # if there are no possible numbers then return False
    # else call backtrack for each possible number and return True if any of these calls return True
    # if all calls returns False, reset that cell with '.' and return False
    p = find_empty_cell(board)
    if p is None:
        return True
    i,j = p
    pvals = possible_values(p, board)
#     print(p, pvals)
    for val in pvals:
        board[i][j] = val
        res = backtrack(board)
        if res:
            return True
        else:
            board[i][j] = '.'
    return False

def fill_single_possible_values(board):
    iterations = 0
    while True:
        single_pos_values_found = False
        iterations = iterations + 1
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    pvals = possible_values((i,j), board)
                    if len(pvals) == 1:
                        board[i][j] = pvals[0]
#                         print(i,j, pvals[0])
                        single_pos_values_found = True
        if not single_pos_values_found:
            print(iterations)
            return
                        
def print_board(board):
    for i in range(9):
        for j in range(9):
            print(board[i][j], end='')
        print('')
            
def solveSudoku(board):
    fill_single_possible_values(board)
    backtrack(board)
    print_board(board)
    
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]]
solveSudoku(board)
#fill_single_possible_values(board)
print_board(board)