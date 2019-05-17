class Player:
    def __init__(self, number):
        self.number = number
        self.points = 0


class Board:
    def __init__(self, size):
        self.size = size
        self.board = []

        for i in range(0, size):
            temp = []
            for j in range(0, size):
                temp.append(0)
            self.board.append(temp)

    def place(self, x, y, player):
        if self.can_be_placed(x, y, self.board):
            self.board[x][y] = player.number
            points = self.calculate_points(x, y, self.board)
            if points:
                player.points += points
            return True
        else:
            return False

    def can_be_placed(self, x, y, board):
        return board[x][y] is 0

    def calculate_points(self, x, y, board):
        points = 0

        # sprawdzam poziomo
        if all(element is not 0 for element in board[x]):
            points += self.size

        # sprawdzam pionowo
        if all(board[i][y] is not 0 for i in range(0, 4)):
            points += self.size

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
            for i, column in zip(range(x, self.size, 1), range(y, self.size, 1)):
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
            for i, col in zip(range(x, -1, -1), range(y, self.size, 1)):
                counter += 1
                if board[i][col] == 0:
                    isFull = False
                    break

        # sprawdzamy dolną lewą przekątną
        if isFull and not (x is 3 or y is 0):
            if counter is not 0:
                counter -= 1
            for i, col in zip(range(x, self.size, 1), range(y, -1, -1)):
                counter += 1
                if board[i][col] == 0:
                    isFull = False
                    break
        if isFull:
            points += counter
        return points

    def print(self):
        for row in self.board:
            print(row)

if __name__ == '__main__':
    gra = Board(4)
    gracz1 = Player(1)
    gracz2 = Player(2)

    gra.place(1,1,gracz1)
    print(gracz1.points, gracz2.points)
    gra.place(0,1,gracz1)
    gra.place(2, 1, gracz2)
    gra.place(3, 1, gracz2)
    gra.print()
    print(gracz1.points, gracz2.points)