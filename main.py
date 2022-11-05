"""
CS664 Connect 4 Final Project
Luke Arpino larpino@bu.edu
Sai Sathvic Reddy kjssr@bu.edu
Ivan Ramadhan ivan2301@bu.edu
Rubeena

"""

# Main class
class Connect4:

    ROW_COUNT = 6
    COL_COUNT = 7

    def __init__(self):
        self.board = []

    def create_board(self):

        # Create the test board
        self.board = [['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_'],
                      ['_', '_', '_', '_', '_', '_', '_']]

    def drop_piece(self, col, player):
        # Check the very top of the row
        print(f"Dropping player {player}'s piece at column: {col}")
        if self.board[0][col] != '_':
            print("")
        else:
            print()
            for x in range(5, -1, -1):
                if self.board[x][col] == '_':
                    self.board[x][col] = self.get_player_piece(player)
                    return

    def get_player_piece(self, player):
        if player == 1:
            return 'X'
        else:
            return 'O'


    def check_for_win(self, player):
        piece = self.get_player_piece(player)
        # Check horizontal
        for c in range(self.COL_COUNT-3):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece \
                        and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True

        # Check vertical
        for c in range(self.COL_COUNT):
            for r in range(self.ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece \
                        and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True

        # Check positive diagonal
        for c in range(self.COL_COUNT-3):
            for r in range(self.ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c+1] == piece \
                        and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                    return True

        # Check negative diagonal
        for c in range(self.COL_COUNT-3):
            for r in range(3, self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece \
                        and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True

    def switch_player(self, player):
        if player == 1:
            return 2
        else:
            return 1

    def show_board(self):
        print("  0 1 2 3 4 5 6")
        count = 0
        for row in self.board:
            print(count, end=" ")
            count += 1
            for col in row:
                print(col, end=" ")
            print()

    def start(self):
        self.create_test_board()

        while True:
            self.show_board()

            direction = input("Enter column number : ")
            print()
            self.input_direction(direction)

    def start(self):
        self.create_board()
        player = 1

        while True:
            print(f"Player {player}'s turn:")
            self.show_board()

            col = int(input("Enter column number : "))
            self.drop_piece(col, player)
            if self.check_for_win(player):
                print(f"PLAYER {player} WON THE GAME")
                self.show_board()
                break

            player = self.switch_player(player)


# starting the game
game = Connect4()
game.start()
