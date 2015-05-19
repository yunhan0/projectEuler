def isPentagonal(n):
	if  ((24 * n + 1) ** .5 + 1 ) % 6 == 0:
		return True
	else:
		return False

def solve(n, k):
	for i in range(k+1, n):
		pn = i * (3 * i - 1) / 2
		pk = (i-k) * (3 * (i-k)-1) / 2
		if isPentagonal(pn - pk) or isPentagonal(pn + pk):
			print pn

N, K = map(int, raw_input().split())
solve(N, K)