def calculate_points(x, y, board):
    points = 0

    # sprawdzam poziomo
    if all(element is not 0 for element in board[x]):
        points += 4

    # sprawdzam pionowo
    if all(board[i][y] is not 0 for i in range(0, 4)):
        points += 4

    # sprawdzam ukosy
    isFull = True
    counter = 0
    # sprawdzamy górną lewą przekątną
    if not (x is 0 or y is 0):
        for i, col in zip(range(x, -1, -1), range(y, -1, -1)):
            counter += 1
            if board[i][col] == 0:
                isFull = False
                break

    # sprawdzamy dolną prawą przekątną
    if isFull and not (x is 3 or y is 3):
        if counter is not 0:
            counter -= 1
        for i, column in zip(range(x, 4, 1), range(y, 4, 1)):
            counter += 1
            if board[i][column] == 0:
                isFull = False
                break
    if isFull:
        points += counter
    counter = 0
    isFull = True

    # sprawdzamy górną prawą przekątną
    if not (x is 0 or y is 3):
        for i, col in zip(range(x, -1, -1), range(y, 4, 1)):
            counter += 1
            if board[i][col] == 0:
                isFull = False
                break

    # sprawdzamy dolną lewą przekątną
    if isFull and not (x is 3 or y is 0):
        if counter is not 0:
            counter -= 1
        for i, col in zip(range(x, 4, 1), range(y, -1, -1)):
            counter += 1
            if board[i][col] == 0:
                isFull = False
                break
    if isFull:
        points += counter
    return points

board = [[1,1,1,1],
         [1,0,1,0],
         [1,1,0,1],
         [0,1,1,1]]
points = calculate_points(2,3,board)
print(points)
for e in board:
    print(e)