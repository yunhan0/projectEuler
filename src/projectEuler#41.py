def seive(n) :
	l = range(0, n+1)
	l[0], l[1] = False, False
	root = int(n ** .5) + 1

	for i in range(0, root):
		if not l[i]:
			continue
		j = i
		while i * j <= n:
			l[i * j] = False
			j += 1
	return [item for item in l if item != False]

primeList = seive(7654322)

def initPandigital(k):
	l = range(1,k+1)
	return set(l)	

def isPandigital(n):
	l = [int(i) for i in str(n)]
	return set(l)

def precomuteList():
	testcase = 10
	l = []
	while testcase <= 1000000000:
		pandiSet = initPandigital(len(str(testcase-1)))
		ret = -1
		for i in primeList:
			if i < (testcase/10):
				continue		
			if i > testcase:
				break
			if isPandigital(i) == pandiSet:
				ret = max(ret, i)
				l.append(ret)
		testcase *= 10
	return l

retList = set(precomuteList())

def solve(n):
	ret = -1
	for x in retList:
		if x > n: 
			break
		if x <= n:
			ret = max(ret, x)
	return ret

T = input()
for i in range(T):
	n = input()
	print solve(n)
