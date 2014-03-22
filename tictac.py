import numpy as np
board = np.chararray((3,3))
board[:] = '_'
print "I challenge you to a game of TIC TAC TOE"
print "You are player X: Your move first!"

#FIND LOCATION FOR X function
#make functions for x turn o turn

x = raw_input("Which row would you like to choose? TOP, MIDDLE, or BOTTOM? ")
y = raw_input("Which column do you choose? LEFT, CENTER, or RIGHT? ")

if x == "TOP":
  row = 0
elif x == "MIDDLE":
  row = 1
elif x == "BOTTOM":
  row = 2
else:
	row = "ERROR"
    
if y == "LEFT":
  col = 0
elif y == "CENTER":
  col = 1
elif y == "RIGHT":
  col = 2
else: 
  col = "ERROR"

for i in np.nditer(board):
  if i == board[row,col]:
    board[row,col] = 'X'
print board
 #need to make sure new board in place with X marked spot before proceding to computer turn

row = np.random.randint(3)
col = np.random.randint(3)#should I change variable names in this function or keep row/col?
for i in np.nditer(board):
  if board[row,col] == '_':
    board[row,col] = 'O'
  elif board != '_':
    row = np.random.randint(3)#how do I account for X or O already on board? look back and change int
    col = np.random.randint(3)
print board



#O'S RANDOM _ REPLACED BY 'COMPUTER' FUNcTION



#PRINT BOARD, BACK TO USER CHOICE
