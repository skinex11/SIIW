import math
import random


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

    def random_game(self, players):
        i = 0
        while self.is_not_full():
            x, y = random.randint(0, self.size-1), random.randint(0, self.size-1)
            # %2 -> zmiana graczy
            if self.place(x, y, players[i % 2]):
                i += 1
        self.print()
        print(players[0].points, players[1].points)

    def is_not_full(self):
        for row in self.board:
            for element in row:
                if element is 0:
                    return True
        return False

    def minmax_game(self, players):
        i = 0
        while self.is_not_full():
            x, y = self.minmax_decision()
            if self.place(x, y, players[i % 2]):
                i += 1
        self.print()
        print(players[0].points, players[1].points)

    def minmax_decision(self):
        best_cordinates = [0, 0]
        best_value = -math.inf

        for x in range(0, self.size):
            for y in range(0, self.size):
                if self.can_be_placed(x, y, self.board):
                    self.board[x][y] = 1
                    #zapisuje punkty za konkretny ruch
                    points = self.calculate_points(x, y, self.board)
                    value = self.minimax(1, False, points, 0)
                    if value > best_value:
                        best_value = value
                        best_cordinates = [x, y]
                    self.board[x][y] = 0
        return best_cordinates

    def minimax(self, cur_depth, maximizing_player, points1, points2):
        if cur_depth is 0 or not self.is_not_full():
            return points1 - points2

        if maximizing_player:
            value = -math.inf

            for x in range (0, self.size):
                for y in range(0, self.size):
                    if self.can_be_placed(x, y, self.board):
                        self.board[x][y] = 1
                        points1 += self.calculate_points(x, y, self.board)
                        value = max(value, self.minimax(cur_depth - 1, 2, points1, points2))
                        self.board[x][y] = 0
        else:
            value = math.inf

            for x in range(0, self.size):
                for y in range(0, self.size):
                    if self.can_be_placed(x, y, self.board):
                        self.board[x][y] = 2
                        points2 += self.calculate_points(x, y, self.board)
                        value = min(value, self.minimax(cur_depth - 1, 1, points1, points2))
                        self.board[x][y] = 0
        return value


if __name__ == '__main__':
    N = 5
    game = Board(N)
    game2 = Board(N)
    p1 = Player(1)
    p2 = Player(2)
    players = [p1, p2]

    game.random_game(players)
    p1.points = 0
    p2.points = 0
    game2.minmax_game(players)
