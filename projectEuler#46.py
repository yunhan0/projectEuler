from __future__ import division

def prime(n):
	l = range(n+1)
	l[0], l[1] = False, False
	limit = int( n ** .5 ) + 1

	for i in range(limit):
		if not l[i]:
			continue
		j = i
		while i * j <= n:
			l[i * j] = False
			j += 1
	return [item for item in l if item != False]

primeList = prime(500000)
primtSet = set(primeList)

def solve(n):
	i = 0
	ret = 0
	while n - primeList[i] > 0:
		left = (n - primeList[i]) / 2
		if left % (left ** .5) == 0:
			ret += 1
		i += 1
	return ret

T = input()
for i in range(T):
	n = input()
	print solve(n)