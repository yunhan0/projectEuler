def minPathSum(M):
	ret = 0
	rows, columns = len(M[0]), len(M)
	# Calculate the bottom row
	for i in range(columns-2, -1, -1):
		M[rows-1][i] += M[rows-1][i+1]
	# Calculate the right row
	for i in range(rows-2, -1, -1):
		M[i][columns-1] += M[i+1][columns-1]

	# Some Dynamic Programing
	for i in range(columns-2, -1, -1):
		for j in range(rows-2, -1, -1):
			M[j][i] += min(M[j+1][i], M[j][i+1])
	return M[0][0]

if __name__ == "__main__":
	T = input();
	M = []
	for i in range(T):
		M.append( map(int, raw_input().split()) );
	print minPathSum(M);