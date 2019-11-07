
# coding: utf-8

# In[1]:


#step 1
from IPython.display import clear_output

def display_board(board):
    clear_output()
    print('|1|2|3|' + '\n' + '|4|5|6|' + '\n' + '|7|8|9|')
    print('|' + board[1] + '|' + board[2] + '|' + board[3] + '|' + '\n' +
          '|' + board[4] + '|' + board[5] + '|' + board[6] + '|' + '\n' +
          '|' + board[7] + '|' + board[8] + '|' + board[9] + '|')


# In[2]:


#step 2
def  player_input():
    player1 = input("First Player, Please Pick a Marker: 'X or 'O'. ")
    while player1.lower() != 'x' and player1.lower() != 'o':
        player1 = input("Error! Please Pick a Marker 'X or 'O'. ")
    player1 = player1.upper()    
    print('First Player Chose ' + player1)
    return player1


# In[3]:


#step 3
def  place_marker(board, marker, position):
    board[position] = marker


# In[4]:


#step 4
def win_check(board, mark):
    wins = [[1,2,3], [1,4,9], [1,5,9], [2,5,8], [3,5,7], [3,6,9], [4,5,6], [7,8,9]]
    for x in wins:
        if board[x[0]] == mark and board[x[1]] == mark and board[x[2]] == mark:
            return True
    return False


# In[5]:


#step 5 
import random

def choose_first():
    first = random.randint(1, 2)
    if first == 1:
        print('Player 1 Goes First.')
    else:
        print('Player 2 Goes First.')


# In[6]:


#step 6
def space_check(board, position):
    if board[int(position)] == 'X' or board[int(position)] == 'O':
        return False
    else:
        return True


# In[7]:


#step 7
def full_board_check(board):
    for x in range(1, 10):
        if board[x] != 'X' and board[x] != 'O':
            return False
    return True


# In[8]:


#step 8
def player_choice(board):
    position = input('Please Enter The Desired Position You Wish to Place Your Piece: ')
    while position in range(1, 10) != True:
        position = input("Error! Please Enter a Number from 1-9.")
    while space_check(board, position) != True:
            position = input('Error! Position Already has a Piece. Please Enter New Position: ')
    return position        


# In[9]:


#step 9
def replay():
    again = input("Do You Want to Play Again? 'Yes' or 'No'?")
    while again.lower() != 'yes' and again.lower() != 'no':
        again = input("Error! Please Answer 'Yes' or 'No'.")
    if again.lower() == 'yes':
        return True
    else:
        return False


# In[10]:


#step 10
print(('Welcome to Tic Tac Toe!'))
print('|1|2|3|' + '\n' + '|4|5|6|' + '\n' + '|7|8|9|')
play = True
while play == True:
    clear_output()
    # Set the game up here
    board = ['#', ' ', ' ',' ',' ',' ',' ',' ',' ',' ']
    print("Choose Which Person is Player 1 and Which is Player 2.")
    pause = input("Press Enter to Continue.")
    choose_first()
    player1 = player_input()
    player2 = ''
    if player1.lower() == 'x':
        player2 = 'O'
    else:
        player2 = 'X'
    print('Second Player, You are ' + player2)
    display_board(board)
    while full_board_check != True:
        print("First Player's Turn")
        position1 = int(player_choice(board))
        place_marker(board, player1, position1)
        display_board(board)
        if win_check(board, player1) == True:
            break
        if full_board_check(board) == True:
            break
        print("Second Player's turn.")
        position2 = int(player_choice(board))
        place_marker(board, player2, position2)
        display_board(board)
        if win_check(board, player2) == True:
            break
    if win_check(board, player1) == True:
        print("Game Over! First Player Won!")
    elif win_check(board, player2) == True:
        print("Game Over! Second Player Won!")
    else:
        print("Game Over! It's a Tie!")
    play = replay()
    if play == False:
        print("Bye!")

