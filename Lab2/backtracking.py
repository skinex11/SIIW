def isSafe(board, row, column, N):
    #sprawdzamy lewą stronę wiersza
    for col in range(column):
        if board[row][col] == 1:
            return False

    #sprawdzamy górną lewą przekątną
    for i, col in zip(range(row, -1, -1), range(column, -1, -1)):
        if board[i][col] == 1:
            return False

    #sprawdzamy dolną lewą przekątną
    for i, col in zip(range(row, N, -1), range(column, -1, -1)):
        if board[i][col] == 1:
            return False

    return True

def solveBackTracking(board, column, N):
    #jeżeli mamy zrobione wszystkie kolumny to zwracamy true
    if column >= N:
        return True

    #dla każdego wiersza
    for row in range(N):
        #jeżeli można wstawić
        if isSafe(board, row, column, N):
            #to wstawiam hetmana
            board[row][column] = 1

            #jeżeli istnieją dalsze rozwiązania to uznaję rozwiązanie za poprawne
            if solveBackTracking(board, column+1, N):
                return True

            #w przeciwnym razie zabieram hetmana
            board[row][column] = 0
    #i zwracam brak rozwiązań
    return False