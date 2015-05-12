def seive(n):
	L = range(n+1)
	L[0], L[1] = False, False
	root = int(n ** .5) + 1
	
	for i in range(root):
		if not L[i]:
			continue
		j = i
		while j * i <= n:
			L[j * i] = False
			j += 1
	return [item for item in L if item != False]

primeList = seive(1000)

def solve(n):
	ways = [1] + [0] * n
	for i in primeList:
		for j in range(i, n+1):
			ways[j] += ways[j-i]
	return ways

ways = solve(1001)

T = input()
for i in range(T):
	N = input()
	print ways[N]