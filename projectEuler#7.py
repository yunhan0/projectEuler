#Algorithm: Sieve of Eratosthenes
def sieve(n):
	l = range(0, n+1)
	l[0], l[1] = False, False
	root = int(n**(0.5)) + 1
	
	for i in range(2, root):
		if not l[i]: continue
		p = i
		while i * p <= n:
			l[i*p] = False
			i += 1
		p += 1
	return [item for item in l if item != False]

l = sieve(200000)

T = int(input())
for i in range(0, T):
	n = int(input())
	print(l[n-1])