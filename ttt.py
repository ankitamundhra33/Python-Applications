# AI based Tic-Tac-Toe
import random

board = [' ' for x in range(10)]


# inserting letter in the board at a particular position
def insertLetter(letter, pos):
    board[pos] = letter


# checking if space is free
def spaceIsFree(pos):
    return board[pos] == ' '


# board structure
def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' ')
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')


# checking if board is full
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


# finding the winner
def isWinner(b, l):
    return ((b[1] == l and b[2] == l and b[3] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or
    (b[7] == l and b[8] == l and b[9] == l) or
    (b[1] == l and b[4] == l and b[7] == l) or
    (b[2] == l and b[5] == l and b[8] == l) or
    (b[3] == l and b[6] == l and b[9] == l) or
    (b[1] == l and b[5] == l and b[9] == l) or
    (b[3] == l and b[5] == l and b[7] == l))


# player move
def playerMove():
    run = True
    while run:
        move = input("Please select a position to place an 'X' (1-9): ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print("Sorry, this space is already occupied!")
            else:
                print('Please type a number between 1-9!')
        except:
            print('Please type a number!')


# computer move
def computerMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    i = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardcopy = board[:]
            boardcopy[i] = let
            if isWinner(boardcopy, let):
                move = i
                return move

    # corner values
    cornersOpen = []
    if i in [1, 3, 7, 9]:
        cornersOpen.append(i)
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # middle value
    if 5 in possibleMoves:
        move = 5
        return move

    # edges values
    edgesOpen = []
    if i in [2, 4, 6, 8]:
        edgesOpen.append(i)
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


# selecting random space
def selectRandom(li):
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


# main logic
def main():
    print('Welcome to Tic-Tac-Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry you lose!')
            break

        if not(isWinner(board, 'X')):
            move = computerMove()
            if move == None:
                print("")
            else:
                insertLetter('O', move)
                print("Computer placed O at position: ", move)
                printBoard(board)
        else:
            print('You Win!')
            break

    if isBoardFull(board):
        print("Its a tie!")

choice = 'y'
while choice == 'y' or choice == 'Y':
    board = [' ' for x in range(10)]
    print('\n')
    main()
    choice = input("Do you want to play again? ")