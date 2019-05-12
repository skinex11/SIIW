def checkForward(board, N, row, col):
    copyBoard = board.copy()

    # sprawdzamy po liniach prostych
    for i in range(N):
        board[i][col] = board[i][col] or 8
        board[row][i] = board[row][i] or 8

    # sprawdzamy dolną prawą przekątną
    for i, column in zip(range(row, N, 1), range(col, -1, -1)):
        board[i][column] = board[i][column] or 8

    # sprawdzamy dolną prawą przekątną
    for i, column in zip(range(row, N, 1), range(col, N, 1)):
        board[i][column] = board[i][column] or 8

    if 0 in board:
        return True, board
    else:
        return False, copyBoard


def forwardChecking(board, N):
    for row in range(N):
        col = 0
        while col < N:
            if board[row][col] == 0:
                board[row][col] = 1
                condition, board = checkForward(board, N, row, col)
                if condition:
                    col = N
                    print(board)
                else:
                    if row == N-1:
                        return board
                    board[row][col] = 8
                    col += 1
            else:
                col += 1
        row += 1
