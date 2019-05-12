from copy import deepcopy

def checkForward(board, N, row, col):
    # sprawdzamy po liniach prostych
    for i in range(N):
        board[i][col] = board[i][col] or 8
        board[row][i] = board[row][i] or 8

    # sprawdzamy dolną prawą przekątną
    for i, column in zip(range(row, N, 1), range(col, -1, -1)):
        board[i][column] = board[i][column] or 8

    # sprawdzamy dolną lewą przekątną
    for i, column in zip(range(row, N, 1), range(col, N, 1)):
        board[i][column] = board[i][column] or 8

    return (board == 0).sum() > N-row-2


def forwardChecking(board, row, N):
    #ustawiamy kolumne na 0
    column = 0
    #dla każdej kolumny
    for col in range(column, N):
        #jeżeli jest możliwe wstawienie hetmana
        if not board[row][col]:
            #kopiuje tablice
            copyBoard = deepcopy(board)
            #wstawiam hetmana
            board[row][col] = 1

            #jeżeli jestem w ostatnim wierszu to drukuje wynik
            if row == N - 1:
                print(board)
                return True

            #sprawdzam czy dla takiego układu dziedzina zawiera następne rozwiązania
            if checkForward(board, N, row, col):
                #jeżeli tak to sprawdzam następny wiersz czy istnieją dla niego rozwiązania
                if forwardChecking(board, row+1, N):
                    return True

                #jeżeli nie istnieją żadne rozwiązania to wracam do wersji z poprzedniego wiersza
                board = deepcopy(copyBoard)
        #i szukam następnego miejsca w tym wierszu do wstawienia hetmana
        col += 1
    #jeżeli nie mogę wstawić żadnego hetmana w tym wierszu to zwracam brak rozwiązań
    return False
