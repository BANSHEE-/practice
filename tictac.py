

#function for player X's move
#need to review indents, do not seem to understand yet (many unindent errors)
def yourmove(board):
  row = raw_input("Which row would you like to choose? TOP, MIDDLE, or BOTTOM? ")
  col = raw_input("Which column do you choose? LEFT, CENTER, or RIGHT? ")
	if row == "TOP":
	  row == 0
	elif row == "MIDDLE":
	  row == 1
	elif row == "BOTTOM":
	  row == 2
	else:
		row = "ERROR. Please indicate TOP, MIDDLE, or BOTTOM row"
#column    
	if col == "LEFT":
	  col == 0
	elif col == "CENTER":
	  col == 1
	elif col == "RIGHT":
	  col == 2
	else: 
	  col == "ERROR. Please indicate LEFT, CENTER, OR RIGHT column"  

  
board[row][col] = 'X'
print board

def compturn(n):
  row = np.random.randint(3)
  col = np.random.randint(3)#should I change variable names in this function or keep row/cow
  board[row][col] = 'O'
  print board

def main():
  import numpy as np
  board = [ [()]*3 for i in range(3) ]
  print board
print "I challenge you to a game of TIC TAC TOE"
print "You are player X: Your move first!"

yourmove(board)
compturn(board)

main()
