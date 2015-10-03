def seive(n):
	l = range(n+1);
	l[0], l[1] = False, False
	root = int(n ** .5) + 1

	for i in range(root):
		if not l[i]:
			continue
		j = i
		while i * j <= n:
			l[i * j] = False
			j += 1
	return [i for i in l if i!= False]

primeList =  seive(100)

def initPandigital(k):
	l = range(1,k+1)
	return set(l)	
	
def solve(n):

n = input()
print solve(n)