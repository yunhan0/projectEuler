MAX_S = 1000
FACTS = [1]

for i in range(1, 1+MAX_S):
	FACTS.append(FACTS[-1]*i)

def choose(n, k):
	return FACTS[n] / (FACTS[k] * FACTS[n-k])

def solve(n, K):
	ret = 0
	for i in range(2, n+1):
		r = 1
		while r <= i: 
			if choose(i, r) > K:
				ret += 1
			r += 1
	return ret

N, K = map(int, raw_input().split())
print solve(N, K)