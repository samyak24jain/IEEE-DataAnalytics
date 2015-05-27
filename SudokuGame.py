from random import randint
from sys import exit

#Logic to check if a particular number can be placed in a particular position.
def logic(i,j,r,sudoku1):
	flag = 0
	for n in range(0,4): #checking if r is already present on the ith row
		if(n != j):
			if(sudoku1[i][n] == r):
				flag = 1
				break
	if(flag == 0):
		for n in range(0,4): #checking if r is already present on the jth row
			if(n != i):
				if(sudoku1[n][j] == r):
					flag = 1
					break
	if(flag == 0):
		if(i <= 1):
			if(j <= 1):
				for x in range(0,2): #checking if r is already present in the cells (0,0),(0,1),(1,0),(1,1) excluding the cell (i,j)
					for y in range(0,2):
						if( x != i and y != j):
							if(r == sudoku1[x][y]):
								flag = 1
								break
					if(flag == 1):
						break
			else:
				for x in range(0,2): #checking if r is already present in the cells (0,2),(0,3),(1,2),(1,3) excluding the cell (i,j)
					for y in range(2,4):
						if(x != i and y != j):
							if(r == sudoku1[x][y]):
								flag = 1
								break
					if(flag == 1):
						break
		else:
			if(j <= 1):
				for x in range(2,4): #checking if r is already present in the cells (2,0),(2,1),(3,0),(3,1) excluding the cell (i,j)
					for y in range(0,2):
						if( x != i and y != j):
							if(r == sudoku1[x][y]):
								flag = 1
								break
					if(flag == 1):
						break
			else:
				for x in range(2,4): #checking if r is already present in the cells (2,2),(2,3),(3,2),(3,4) excluding the cell (i,j)
					for y in range(2,4):
						if(x != i and y != j):
							if(r == sudoku1[x][y]):
								flag = 1
								break
					if(flag == 1):
						break
	return flag

#Completely Solved Random Sudoku Generator
def GenerateSudoku(sudoku2):	
	for i in range(0,4):
		for j in range(0,4):
			flag1 = 0
			while (flag1 == 0):	
				r = randint(1,4)  #assigning random number to r in the range(1,4)
				flag1 = logic(i,j,r,sudoku2) #checking if its possible to place the number there
				if(flag1 == 0):
					sudoku2[i][j] = r
					break
				else:
					flag1 = 0;
	return sudoku2

#Forms unsolved sudoku from solved sudoku by removing 9 random numbers and prints it
def PrintUnsolvedSudoku():
	sudoku = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
	sudoku = GenerateSudoku(sudoku)
	count = 0
	while 1 :
		x = randint(0,3)
		y = randint(0,3)
		if(sudoku[x][y] != '_'):
			sudoku[x][y] = '_'
			count += 1
		if(count == 9):
			break
	for i in range(0,4):
		for j in range(0,4):
			print sudoku[i][j]," ",
		print "\n"
	return sudoku

#Receives input from the user and checks validity
def UserInput(check):
	count = 0
	while(count < 9):
		while(1):
			print "\nEnter position you want to fill :"
			row = int(raw_input("> Enter row number(0-3) : "))
			col = int(raw_input("> Enter column number(0-3) : "))
			num = int(raw_input("> Enter number(1-4) : "))
			if(row < 0 or row > 3 or col <0 or col > 3 or num < 1 or num > 4):
				print "INVALID INPUT! Please try again."
				continue
			elif(check[row][col] != '_'):
				print "This position is already filled! Please try again"
				continue
			else:
				break
		flag2 = logic(row,col,num,check)
		if(flag2 == 0):
			print "\nPossible!"
			check[row][col] = num
			count = count + 1
			for i in range(0,4):
				for j in range(0,4):
					print check[i][j]," ",
				print "\n"
		elif flag2 == 1 :
			option = raw_input("\nNot Possible! Do you want to Quit or Try again? (Q/T) : ")
			if(option == 'Q'):
				print "-----------------------------------------------------------------------------------------------------"
				print "\t\t\t\t\tPLAYER QUIT! GAME OVER!"
				print "-----------------------------------------------------------------------------------------------------"
				raw_input()
				exit(0)
			elif(option == 'T'):
				continue
		if(count == 9):
			break
	print "-----------------------------------------------------------------------------------------------------"
	print "\t\t\t\t\tCONGRATULATIONS! YOU WIN THE GAME!!"	
	print "-----------------------------------------------------------------------------------------------------"

#Calling all functions in order
print "-----------------------------------------------------------------------------------------------------"
print "\t\t\t\t\tLET'S PLAY SUDOKU!"
print "-----------------------------------------------------------------------------------------------------"
unsolved_sudoku = PrintUnsolvedSudoku()
UserInput(unsolved_sudoku)
raw_input()