import numpy as np
board={}
for int in range(9):
    board.update({int:'_'})


xtaken = []#use x and otaken to confirm a win
otaken =[]
taken = []

def viewboard():
	view = board.values()
	for i in xrange(0,len(view),3):
		print view[i:i+3]


def xmove():
	row = raw_input("Pick a row: ")
	col = raw_input("Pick a col: ")
	if row == "Top":
		x = 0
	elif row == "Middle":
		x = 3
	elif row == "Bottom":
		x = 6

	if col == "Left":
		x += 0
	elif col == "Center":
		x += 1
	elif col == "Right":
		x += 2
	
	if x not in taken:
		board.update({x:'X'})
		xtaken.append(x)
		taken.append(x)
		print board
	else:
		x = np.random.randint



#after two move comp stops working HELP
def compwrite(pos):#does this argument need to be here?
		board.update({pos:'O'})
		otaken.append(pos)
		taken.append(pos)
		print board

def compmove():
    pos = np.random.randint(8)
    if pos not in taken:
				compwrite(pos)
				print board
    else:#how do we make it go back through random integer loop if already in take? call function again until integer that works?
        pos = np.random.randint(8)

count = 0
while count < 10:
    xmove()
    compmove()

    viewboard()
    print otaken
    print xtaken
    count += 1

#board formating (turn to its won function to use after each turn
