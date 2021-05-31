import time

turn = 'X'
move_count = 0
winner = None


def new_board():
    return {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


the_board = new_board()


def printBoard(board: dict):
    print()
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']}")
    print('-+-+-')
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']}")
    print('-+-+-')
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']}")
    print()


def boardWithNames():
    board = 'top-L|top-M|top-R\n' \
            '-----+-----+-----\n' \
            'mid-L|mid-M|mid-R\n' \
            '-----+-----+-----\n' \
            'low-L|low-M|low-R'

    return board


def getNextTurn():
    global turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'


def reset_game():
    global the_board, move_count
    the_board = new_board()
    move_count = 0


def nobody_won():
    print("Nobody won...")
    print("Restarting game...")
    time.sleep(3)
    reset_game()


def checkWinner(board: dict):
    if board['top-L'] == board['top-M'] == board['top-R'] != ' ':
        return True
    elif board['top-L'] == board['mid-L'] == board['low-L'] != ' ':
        return True
    elif board['top-L'] == board['mid-M'] == board['low-R'] != ' ':
        return True
    elif board['top-M'] == board['mid-M'] == board['low-M'] != ' ':
        return True
    elif board['top-R'] == board['mid-R'] == board['low-R'] != ' ':
        return True
    elif board['top-R'] == board['mid-M'] == board['low-L'] != ' ':
        return True
    elif board['mid-L'] == board['mid-M'] == board['mid-R'] != ' ':
        return True
    elif board['low-L'] == board['low-M'] == board['low-R'] != ' ':
        return True
    else:
        return False


while True:
    move_count += 1
    printBoard(the_board)
    print(f"Turn for {turn}. Move on which space?")
    print(boardWithNames())
    move = input()
    if move in the_board.keys():
        if the_board[move] == ' ':
            the_board[move] = turn
            if checkWinner(the_board):
                winner = turn
                print(f"{turn} is the Winner!")
                break
            getNextTurn()

        else:
            print('This space is already chosen.')
            move_count -= 1
    else:
        move_count -= 1
        print("Please, enter valid input")

    if move_count == 9:
        nobody_won()
