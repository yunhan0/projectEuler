MOD = 1000000007

def solve(n):
	ways = [1] + [0] * n	
	for i in range(1, n):
		for j in range(i, n+1):
			ways[j] = (ways[j] + ways[j-i]) % MOD
	return ways

ways = solve(1001)

T = input()
for i in range(T):
	n = input()
	print ways[n] - 1
