
import random

def drawBoard(board):
    print('   |   |')
    print(' '+ board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' '+ board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('------------')
    print('   |   |')
    print(' '+ board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')




print('                   Tic Tac Toe   \n')
theBoard = [' ']*10


winner(0)
drawBoard(theBoard)
print("                    Player vs. Computer\n")
print("Do you want to be X or O? ")
letter = input().upper()
# the first element in the list is the player’s letter, the second is the computer's letter.
if letter == 'X':
      Assign =  ['X', 'O']
else:
      Assign =  ['O', 'X']

while(winner==0):
   if z%2 == 0:
      print("Choose a spot 1-9")
      spot = input()
      drawBoard(board[spot])

