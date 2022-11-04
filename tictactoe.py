"""
CS664 Lab1 Tic Tac Toe
Luke Arpino larpino@bu.edu
Sai Sathvic Reddy kjssr@bu.edu
Ivan Ramadhan ivan2301@bu.edu

"""

import random

the_board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]


def get_random_first_player():
    return random.randint(0, 1)


def fix_spot(board, row, col, player):
    board[row][col] = player


def is_player_win(board, player):
    win = None
    n = len(board)

    # checking rows
    for i in range(n):
        win = True
        for j in range(n):
            if board[i][j] != player:
                win = False
                break
        if win:
            return win

    # checking columns
    for i in range(n):
        win = True
        for j in range(n):
            if board[j][i] != player:
                win = False
                break
        if win:
            return win

    # checking diagonals
    win = True
    for i in range(n):
        if board[i][i] != player:
            win = False
            break
    if win:
        return win

    win = True
    for i in range(n):
        if board[i][n - 1 - i] != player:
            win = False
            break
    if win:
        return win
    return False



def is_board_filled(board):
    for row in board:
        for item in row:
            if item == ' ':
                return False
    return True


def swap_player_turn(player):
    if player == 'O':
        return 'X'

    if player == 'X':
        return 'O'


def show_board(board):
    print("  0 1 2")
    count = 0
    for row in board:
        print(count, end=" ")
        count += 1
        for item in row:
            print(item, end=" ")
        print()


def check_for_pocket(board):
    n = len(board)
    symbol_count = 0  # count of player symbols
    blank_count = 0  # count of blank spaces

    if board[1][0] == board[0][1] != ' ':
        if board[0][0] == ' ':
            return 0, 0
    if board[1][2] == board[0][1] != ' ':
        if board[0][2] == ' ':
            return 0, 2
    if board[1][2] == board[2][1] != ' ':
        if board[2][2] == ' ':
            return 2, 2
    if board[1][0] == board[2][1] != ' ':
        if board[2][0] == ' ':
            return 2, 0

    return False

def check_for_2(board, player):
    # this function checks the board for any rows cols or diags where there is a blank space and 2 of the same character
    # ie a win or a block scenario
    # returns a row, col tuple at the blank space if there is a 2 in a row, or returns false if not

    n = len(board)

    symbol_count = 0  # count of player symbols in rows
    blank_count = 0  # count of blank spaces

    # check rows
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                symbol_count += 1

            elif board[i][j] == ' ':
                blank_count += 1
                blank = i, j

        if (symbol_count == 2) & (blank_count == 1):
            return blank

        symbol_count = 0  # count of player symbols in rows
        blank_count = 0  # count of blank spaces

    # check columns
    for i in range(n):
        for j in range(n):
            if board[j][i] == player:
                symbol_count += 1

            elif board[j][i] == ' ':
                blank_count += 1
                blank = j, i

        if (symbol_count == 2) & (blank_count == 1):
            return blank

        symbol_count = 0  # count of player symbols in cols
        blank_count = 0  # count of blank spaces

    # check diagonal1
    for i in range(n):
        if board[i][i] == player:
            symbol_count += 1
        elif board[i][i] == ' ':
            blank_count += 1
            blank = i, i

    if (symbol_count == 2) & (blank_count == 1):
        return blank

    symbol_count = 0  # count of player symbols in diagonal
    blank_count = 0  # count of blank spaces

    # check diagonal2
    for i in range(n):
        if board[i][n - 1 - i] == player:
            symbol_count += 1
        elif board[i][n - 1 - i] == ' ':
            blank_count += 1
            blank = i, n - 1 - i

    if (symbol_count == 2) & (blank_count == 1):
        return blank

    return False


def agent(board, player1):
    # this function takes a player symbol,
    # and returns a position tuple representing where that player should place their piece

    player2 = 'O'
    if player1 == 'O':
        player2 = 'X'

    # check for win
    check = check_for_2(board, player1)
    if check:
        return check

    # check for block
    check = check_for_2(board, player2)
    if check:
        return check

    # check if a corner pocket needs to be blocked
    check = check_for_pocket(board)
    if check:
        return check


    # take center
    if board[1][1] == ' ':
        return 1, 1

    # take corner
    corners = [[0, 0], [0, 2], [2, 0], [2, 2]]
    for corner in corners:
        row = corner[0]
        col = corner[1]
        if board[row][col] == ' ':
            return row, col

    while True:
        result = random.randint(0, 2), random.randint(0, 2)
        if board[result[0]][result[1]] == ' ':
            break

    return result


print("Human is X. Flipping coin.")

if get_random_first_player() == 1:
    the_player = 'X'
else:
    the_player = 'O'

while True:

    show_board(the_board)
    print(f"Player {the_player} turn")

    if the_player == 'X':
        # taking user input
        row, col = list(
            map(int, input("Enter row and column numbers to fix spot [format: row space col] : ").split()))
        print()
        fix_spot(the_board, row, col, the_player)
    else:
        row, col = agent(the_board, 'O')
        fix_spot(the_board, row, col, the_player)

    # checking whether current player is won or not
    if is_player_win(the_board, the_player):
        print(f"Player {the_player} wins the game!")
        break

    # checking whether the game is draw or not
    if is_board_filled(the_board):
        print("Match Draw!")
        break

    # swapping the turn
    print("swapping the turn")
    if the_player == 'X':
        the_player = 'O'
    elif the_player == 'O':
        the_player = 'X'

# showing the final view of board
print()
show_board(the_board)
