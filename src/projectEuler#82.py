def minPathSum(M):
	rows, columns = len(M[0]), len(M)
	# set initial cost list as the most right column
	cost = [ M[i][-1] for i in range(columns) ]
	# start from the last second column and the second row.
	for j in xrange(columns-2, -1, -1):
		cost[0] += M[0][j]
		for i in range(1, rows):
			cost[i] = min(cost[i], cost[i-1]) + M[i][j]
		# except the bottom row, other rows can move down
		for i in xrange(rows-2, -1, -1):
			cost[i] = min(cost[i], cost[i+1] + M[i][j])
	return min(cost)


if __name__ == "__main__":
	T = input();
	M = []
	for i in range(T):
		M.append( map(int, raw_input().split()) );
	print minPathSum(M);