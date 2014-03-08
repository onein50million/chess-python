import os
# coding: utf-8

os.system("clear")
board = []
blackBoardOrder = ["♜ ","♞ ","♝ ","♛ ","♚ ","♝ ","♞ ","♜ ","♟ ","♟ ","♟ ","♟ ","♟ ","♟ ","♟ ","♟ "]
whiteBoardOrder = ["♙ ","♙ ","♙ ","♙ ","♙ ","♙ ","♙ ","♙ ","♖ ","♘ ","♗ ","♕ ","♔ ","♗ ","♘ ","♖ "]
turn = 0
numbers = []


for i in range(0,8):
	numbers.append(str(i)+" ")

for i in range(0,64):
	board.append("  ")

def inputError():
	print "Error in input, please try again"

def displayBoard():

	print "  "+"".join(numbers)


	for i in range(0,len(board),8):
		print i/8,
		print "".join(board[i:i+8])

def placePiece(x,y,piece):
	index = y * 8 + x
	board[index] = piece

def removePiece(x,y):
	index = y * 8 + x
	board[index] = "  "

def movePiece(x1,y1,x2,y2):
	index1 = y1 * 8 + x1
	index2 = y2 * 8 + x2
	oldPiece = board[index1]
	removePiece(x1,y1)
	placePiece(x2,y2,oldPiece)

def getInt(text):
	while  True:
		var = raw_input(text)
		try:
			return int(var)
		except ValueError:
			print("Invalid input. Please enter a number")
			continue

#def updateBoard():
#	print "" * 16
#	displayBoard()

def generateBoard():
	for i in range(0,len(blackBoardOrder)):
		placePiece(i%8,int(i/8),blackBoardOrder[i])

	for i in range(0,len(whiteBoardOrder)):
		placePiece(i%8,int(i/8)+6,whiteBoardOrder[i])
	
generateBoard()

displayBoard()

while True:
	if turn%2 == 0:
		print "White's Turn"
	else:
		print "Black's Turn"


	moveFromx = getInt("Move From(x):")
	moveFromy = getInt("Move from(y):")
	moveTox = getInt("Move to(x):")
	moveToy = getInt("Move to(y):")

	movePiece(moveFromx,moveFromy,moveTox,moveToy)

	turn += 1

	os.system("clear")

	displayBoard()
