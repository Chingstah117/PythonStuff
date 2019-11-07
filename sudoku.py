#imports the list of numbers allowed in sudoku [1:9] so that numbers can be randomly used for the testBoard() code
import random
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]



#prints out numbers of the sudoku board given from the testBoard() code into lists by row so that 
#they can be used to print out the visual board in later code
def makeBoard():
    board = None
    while board is None:
        board = testBoard()
    return board



#used to bold directions and phrases in the game
beginning = "\033[1m"
end = "\033[0;0m"



#goes through the board and tests numbers in order to figure out what numbers go where in order to correctly fill up
#a sudoku board, gives a random board each time by taking numbers from the randonmly shuffled numbers list each time
def testBoard():
    board = [[None for _ in range(9)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            check = numbers[:]
            random.shuffle(check)
            x = -1
            loopStart = 0
            while board[i][j] is None:
                x += 1
                if x == 9:
                    return None
                checknumber = [check[x], True]
                if checknumber in board[i]:
                    continue
                checkis = False
                for checkRow in board:
                    if checkRow[j] == checknumber:
                        checkis = True
                if checkis: continue
                if i % 3 == 1:
                    if   j % 3 == 0 and checknumber in (board[i - 1][j + 1], board[i - 1][j + 2]): continue
                    elif j % 3 == 1 and checknumber in (board[i - 1][j - 1], board[i - 1][j + 1]): continue
                    elif j % 3 == 2 and checknumber in (board[i - 1][j - 1], board[i - 1][j - 2]): continue
                elif i % 3 == 2:
                    if   j % 3 == 0 and checknumber in (board[i - 1][j + 1], board[i - 1][j + 2], board[i - 2][j + 1], board[i - 2][j + 2]): continue
                    elif j % 3 == 1 and checknumber in (board[i - 1][j - 1], board[i - 1][j + 1], board[i - 2][j - 1], board[i - 2][j + 1]): continue
                    elif j % 3 == 2 and checknumber in (board[i - 1][j - 1], board[i - 1][j - 2], board[i - 2][j - 1], board[i - 2][j - 2]): continue
                board[i][j] = checknumber
    return board



#prints the board with the correct numbers given from the makeBoard code with borders
#that make it easier for the user to see the blocks of 9 
def printBoard(board):
    border = "+---+---+---++---+---+---++---+---+---+"
    print (border.replace('-', '='))
    for i, line in enumerate(board):
        print ("| {} | {} | {} || {} | {} | {} || {} | {} | {} |".format(
                    line[0][0] if line[0][1] else ' ',
                    line[1][0] if line[1][1] else ' ',
                    line[2][0] if line[2][1] else ' ',
                    line[3][0] if line[3][1] else ' ',
                    line[4][0] if line[4][1] else ' ',
                    line[5][0] if line[5][1] else ' ',
                    line[6][0] if line[6][1] else ' ',
                    line[7][0] if line[7][1] else ' ',
                    line[8][0] if line[8][1] else ' ',))
        if (i + 1) % 3 == 0: print(border.replace('-', '='))
        else: print(border)



#makes 2 copies of the board, so that the user changes board a, but board b
#is still the original so that the checkanswers code still works
import copy
b = makeBoard()
a = copy.deepcopy(b)



#begins the game by asking for difficulty level
def start():
    print beginning + 'What level difficulty would you like to play? Type "easy()", "intermediate()" or "hard()"' + end


#list of spaces on the board that are deleted when the user wants a easy board
#used so that even though there are random boards made each time, the easy 
#level always has 35 blank spaces, also prints out the board and directions for how to play
def easy():
    for index in [2, 4, 5]:
        a[0][index] = [0, True]
    for index in [0, 3, 4, 7]:
        a[1][index] = [0, True]
    for index in [4, 5, 6, 8]:
        a[2][index] = [0, True]
    for index in [0, 2, 3, 5, 6]:
        a[3][index] = [0, True]
    for index in [2, 5, 7, 8]:
        a[4][index] = [0, True]
    for index in [1, 3]:
        a[5][index] = [0, True]
    for index in [0, 3, 6, 7, 8]:
        a[6][index] = [0, True]
    for index in [1, 2, 5, 8]:
        a[7][index] = [0, True]
    for index in [1, 5, 6, 8]:
        a[8][index] = [0, True]
    print beginning + 'Directions: Each 0 on the board is a blank space that you need to fill in. To input a number, type "input(row, column, guess)". If you are stuck, type "hint()" to get 1 space filled in. You only have 3 hints! Once you have finished, type "checkanswers()". If the entire board is correct, you will receive a "You win!" message, or else you will receive a "Keep trying!" message. Good luck!' + end
    printBoard(a)


#list of spaces on the board that are deleted when the user wants a intermediate board
#used so that even though there are random boards made each time, the intermediate 
#level always has 45 blank spaces, also prints out the board and directions for how to play
def intermediate():
    for index in [0, 2, 4, 8]:
        a[0][index] = [0, True]
    for index in [0, 2, 3, 4, 6, 7]:
        a[1][index] = [0, True]
    for index in [0, 4, 5, 6, 8]:
        a[2][index] = [0, True]
    for index in [0, 2, 3, 5, 6]:
        a[3][index] = [0, True]
    for index in [2, 5, 7, 8]:
        a[4][index] = [0, True]
    for index in [1, 2, 3, 5, 7]:
        a[5][index] = [0, True]
    for index in [0, 1, 3, 6, 7, 8]:
        a[6][index] = [0, True]
    for index in [1, 2, 5, 7, 8]:
        a[7][index] = [0, True]
    for index in [1, 5, 6, 8]:
        a[8][index] = [0, True]
    print beginning + 'Directions: Each 0 on the board is a blank space that you need to fill in. To input a number, type "input(row, column, guess)". If you are stuck, type "hint()" to get 1 space filled in. You only have 3 hints! Once you have finished, type "checkanswers()". If the entire board is correct, you will receive a "You win!" message, or else you will receive a "Keep trying!" message. Good luck!' + end
    printBoard(a)



#list of spaces on the board that are deleted when the user wants a hard board
#used so that even though there are random boards made each time, the hard 
#level always has 55 blank spaces, also prints out the board and directions for how to play
def hard():
    for index in [0, 2, 4, 5, 7, 8]:
        a[0][index] = [0, True]
    for index in [1, 2, 3, 4, 6, 7]:
        a[1][index] = [0, True]
    for index in [0, 4, 5, 6, 8]:
        a[2][index] = [0, True]
    for index in [0, 2, 3, 5, 6, 7, 8]:
        a[3][index] = [0, True]
    for index in [1, 2, 4, 5, 7, 8]:
        a[4][index] = [0, True]
    for index in [1, 2, 3, 5, 7, 8]:
        a[5][index] = [0, True]
    for index in [0, 1, 2, 3, 6, 7, 8]:
        a[6][index] = [0, True]
    for index in [1, 2, 5, 6, 7, 8]:
        a[7][index] = [0, True]
    for index in [1, 3, 5, 6, 7, 8]:
        a[8][index] = [0, True]
    print beginning + 'Directions: Each 0 on the board is a blank space that you need to fill in. To input a number, type "input(row, column, guess)". If you are stuck, type "hint()" to get 1 space filled in. You only have 3 hints! Once you have finished, type "checkanswers()". If the entire board is correct, you will receive a "You win!" message, or else you will receive a "Keep trying!" message. Good luck!' + end
    printBoard(a)

#takes the row, col, and guess that the player inputs and puts that into correct space on the board,
#it prints a new board with only that space changed
def input(row, column, guess):
     for i in range(1,10):
         if row == i:
            a[i - 1][column - 1] = [guess, True]
            printBoard(a)



#when the player types hint(), one space is filled in with the correct number 
#that is given from board b. We have only allowed hint to run 3 times, therefore the 
#loop breaks once k is greater than 3, k tracks the number of times that hint has been run
#if a hint is used, the new board appears with the hint number, or else no new board is outputted
def hint(k=[0]):
    k[0]+=1 
    if k[0] < 4:
        for i in range(0,9):
            for j in range (0,9):
                if a[i][j] == [0, True]:
                    a[i][j] = b[i][j]
                    break
            break
        printBoard(a)
        print 'This is hint number', k[0]  
    else: 
        print 'You have no hints left' 



#if a(the board that the player has been inputting numbers into) 
#equals b(the original board with all values already filled in), 
#then the user has correctly filled in thes spaces and gets a winning message
#if not, they will be told to keep trying
def checkanswers(): 
    if a == b:
        print beginning + 'You win!' + end
    else:
        print beginning + 'Keep trying!' + end