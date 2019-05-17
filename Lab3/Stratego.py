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

    def place(self, x, y, player, board):
        if self.can_be_placed(x, y, board):
            board[x][y] = player.number
            points = self.calculate_points(x, y, board)
            if points:
                player.points += points
            return True
        else:
            return False

    def can_be_placed(self, x, y, board):
        return board[x][y] is 0

    def calculate_points(self, x, y, board):
        points = 0

        #sprawdzam poziomo
        if any(element is 0 for element in board[x]):
            points += self.size

        #sprawdzam pionowo
        if any(board[i][y] is 0 for i in range(0, self.size)):
            points += self.size

        
