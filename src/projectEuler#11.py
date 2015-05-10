def greatestProduct(M):
	ret, tmp = 0, 0
	for i in range(20):
		for j in range(17):
			#left right
			tmp = M[i][j] * M[i][j+1] * M[i][j+2] * M[i][j+3]
			ret = max(ret, tmp)
			#up down
			tmp = M[j][i] * M[j+1][i] * M[j+2][i] * M[j+3][i]
			ret = max(ret, tmp)

	#diagonally
	for i in range(17):
		for j in range(17):
			tmp = M[i][j] * M[i+1][j+1] * M[i+2][j+2] * M[i+3][j+3]
			ret = max(ret, tmp)
	for i in range(3, 20):
		for j in range(17):
			tmp = M[i][j] * M[i-1][j+1] * M[i-2][j+2] * M[i-3][j+3]
			ret = max(ret, tmp)
	print ret

M = []
for i in range(20):
	n = raw_input().split()
	n = [int(i) for i in n]
	M.append(n)

greatestProduct(M)