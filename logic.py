import random

class Game:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.leaveLoop = False
        self.turn = 'X'
        self.turnCounter = 0
        self.board = self.make_empty_board()

    def make_empty_board(self):
        return [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]

    def print_board(self):
        for x in range(self.rows):
            print("\n-|---|---|---|-")
            print(" |", end="")
            for y in range(self.cols):
                print("", self.board[x][y], end=" |")
        print("\n-|---|---|---|-")

    def get_winner(self):
        for x in range(3):
            if self.board[x][0] == self.board[x][1] == self.board[x][2]:
                return self.board[x][0]
            elif self.board[0][x] == self.board[1][x] == self.board[2][x]:
                return self.board[0][x]
            # Check for diagonal
            elif self.board[0][0] == self.board[1][1] == self.board[2][2]:
                return self.board[0][0]
            elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
                return self.board[0][2]
        # If there's no winner
        return "N"

    def other_player(self):
        if self.turn == 'X':
            self.turn = 'O'
        elif self.turn == 'O':
            self.turn = 'X'

    def modify_array(self, num):
        num -= 1
        if num == 0:
            self.board[0][0] = self.turn
        elif num == 1:
            self.board[0][1] = self.turn
        elif num == 2:
            self.board[0][2] = self.turn
        elif num == 3:
            self.board[1][0] = self.turn
        elif num == 4:
            self.board[1][1] = self.turn
        elif num == 5:
            self.board[1][2] = self.turn
        elif num == 6:
            self.board[2][0] = self.turn
        elif num == 7:
            self.board[2][1] = self.turn
        elif num == 8:
            self.board[2][2] = self.turn

    def choose_players():
        while True:
            try:
                num_players = int(input("Enter the number of players (1 or 2): "))
                if num_players in [1, 2]:
                    return num_players
                else:
                    print("Invalid input. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    def choose_players():
        while True:
            try:
                num_players = int(input("Enter the number of players (1 or 2): "))
                if num_players in [1, 2]:
                    return num_players
                else:
                    print("Invalid input. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter a number.")
            
class Human(Game):
    def __init__(self):
        super().__init__()

    def make_move(self):
        valid_move = False
        while not valid_move:
            try:
                move = int(input("Enter your move (1-9): "))
                if 1 <= move <= 9 and isinstance(self.board[(move - 1) // 3][(move - 1) % 3], int):
                    valid_move = True
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        return move


class Bot(Game):
    def __init__(self):
        super().__init__()

    def make_move(self):
        available_moves = [i for i in range(1, 10) if isinstance(self.board[(i - 1) // 3][(i - 1) % 3], int)]
        move = random.choice(available_moves)
        return move
    
game = Game()
human_player = Human()
bot_player = Bot()
