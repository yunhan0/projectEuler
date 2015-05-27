def seive(n):
	l = range(0,n+1)
	l[0], l[1] = False, False
	root = int(n ** .5) + 1

	for i in range(root):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[j * i] = False
			j += 1
	return [i for i in l if i != False]

def quadratic(a, b, n):
	return n * n + a * n + b

def solve(N):
	primeList = seive(N)
	ret, amax, bmax = 0, 0, 0
	for b in primeList:
		for a in range(-b, b, 2):
			n = 0
			while quadratic(a, b, n) in primeSet:				
				n += 1
			if n > ret:
				ret, amax, bmax = n, a, b
	print amax, bmax

if __name__ == "__main__":
	primeSet = set(seive(2000))
	N = input()
	solve(N-1)