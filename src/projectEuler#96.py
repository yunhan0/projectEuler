def isFull(board):
	for i in range(0,9):
		for j in range(0,9):
			if board[i][j] == 0:
				return False
	return True

def possibleEntries(board, i, j):
	possibleArray = {}

	for x in range(1, 10):
		possibleArray[x] = 0

	# Horizontal 
	for y in range(0, 9):
		if not board[i][y] == 0:
			possibleArray[board[i][y]] = 1
	# Vertical
	for x in range(0, 9):
		if not board[x][j] == 0:
			possibleArray[board[x][j]] = 1
	# Box
	k = 0
	l = 0
	if i >= 0 and i <= 2:
		k = 0
	elif i >= 3 and i <= 5:
		k = 3
	else:
		k = 6

	if j >= 0 and j <= 2:
		l = 0
	elif j >= 3 and j <= 5:
		l = 3
	else:
		l = 6
	for x in range(k, k + 3):
		for y in range(l, l + 3):
			if not board[x][y] == 0:
				possibleArray[board[x][y]] = 1

	for x in range(1, 10):
		if possibleArray[x] == 0:
			possibleArray[x] = x
		else:
			possibleArray[x] = 0
	return possibleArray

def printBoard(board):
	for i in range(0, len(board)):
		print "".join(map(str, board[i]))

def sudokuSolver(board):
	i = 0
	j = 0
	possibilities = {}

	if isFull(board):
		printBoard(board)
	else:
		# find first vacant place
		for x in range(0, 9):
			for y in range(0, 9):
				if board[x][y] == 0:
					i = x
					j = y
					break
			else:
				continue
			break

		possibilities = possibleEntries(board, i, j)

		for x in range(1, 10):
			if not possibilities[x] == 0:
				board[i][j] = possibilities[x]
				sudokuSolver(board)
		# Backtrack
		board[i][j] = 0

board = []
if __name__ == "__main__":
	lines = 9
	for i in range(lines): 
		line = map(int, list(raw_input()))
		board.append(line)
	sudokuSolver(board)