from __future__ import division
def sieve(n):
	l = range(0, n+1)
	l[0], l[1] = False, False
	root = int( n ** .5 ) + 1
	
	for i in range(2,root):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[j * i] = False
			j += 1
	return [item for item in l if item != False]

pList = set(sieve(1000))

def totient(n):
	ret = n
	i = 2
	while i * i <= n:
		if n % i == 0 and i in pList:
			ret *= ((i-1)/ i)
			while n%i == 0:
				n /= i
		i += 1
	if n > 1:
		ret *= ((n-1)/ n)
	return int(ret)

def solve(n):
	l = [0] * (n+1)
	for i in range(2, n+1):
		l[i] = totient(i) + l[i - 1]
	return l

l = solve(1000000)

T = input()
for i in range(T):
	n = input()
	print l[n]