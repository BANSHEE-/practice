digits = eval(raw_input("Enter a 16 digit number:"))
#use raw_input!! note: eval(input())'s input must be a string (in python3 you can just use input() for raw)
#cant use raw_inputs in ipython *yet*
digstr = str(digits)
#what is zeropadding a string? do I need to set parameters that take it into account for a valid number?
#should this be its own function? what is best for readibility?
#use while loop instead of if so the error message will continue while digits incorrect --- if you use 'if' loop onle one error message then it is done
while len(digstr) != 16:

	digits = eval(raw_input("Try again. Enter a *16* digit number:"))
	digstr = str(digits) #have to convert int value back to string in order for loop to work

#LUHN'S ALGORITHM 
#make seperate functions for all of these? use iterations of range to get odd and even-- or just make new substrings

odds = digstr[1:len(digstr)+1:2] #do I need to add one to len() to contain all elements of list?
print odds
evens = digstr[0:len(digstr):2]#it doesnt look like- but you should LOOK THIS UP!
print evens
newodds = []

finalsum = 0
for i in odds:
#WARNING! DO NOT DO THIS: newodds.append(i*2) it's a string give element twice and does not multiply value! convert back to an int!!!
  j = int(i)
  j = (j*2)
  finalsum += j
#test
print finalsum
for k in evens:
    finalsum += int(k)
#test
print finalsum

if finalsum % 10 == 0:
  print ("Valid Credit Card Number")
else:
	print ("Invalid Credit Card Number")

