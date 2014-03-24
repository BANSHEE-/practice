

import numpy as np
board = [ [()]*3 for i in range(3) ]
row = 0
col = 0
comprow = 0
compcol = 0


#WHY DO I KEEP GETTING INDENT ERRORS!!!
def yourmove(row, col): #keep figuring out defining parameters for function, flow of execution, at what point do variables need to be defined
  x = raw_input("Which row would you like to choose? TOP, MIDDLE, or BOTTOM? ")
  y = raw_input("Which column do you choose? LEFT, CENTER, or RIGHT? ")

  if x == "TOP":
 		row += 0
  elif x == "MIDDLE":
 		row += 1
  elif x == "BOTTOM":
 		row += 2
  elif y == "LEFT":
    col += 0
  elif y == "CENTER":
    col += 1
  elif y == "RIGHT":
    col += 2
  
  board[row][col] = 'X'


def compmove(comprow,compcol):
  comprow += np.random.randint(3)
  compcol += np.random.randint(3)#should I change variable names in this function or keep row/cow
  for i in range(len(board)):
    if board[comprow][compcol] != ('X' or 'O'):#range len for nested list
      board[comprow][compcol] = 'O'
  return board







yourmove(row, col)
compmove(comprow, compcol)
print board


