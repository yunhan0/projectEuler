def initPandigital(k):
	l = range(1,k+1)
	return set(l)

def isPandigital(n):
	l = [int(i) for i in str(n)]
	return set(l)

def solve(n):
	pandiSet = initPandigital(n)
	limit = 10 ** (n - 1)
	root = int(limit ** .5) + 1
	ret = []
	for i in range(1, root):
		j = i
		s = str(i) + str(j) + str(i * j)
		if len(s) > n:
			break
		while len(s) <= n:
			mul = i * j
			s = str(i) + str(j) + str(mul)
			if isPandigital(s) == pandiSet:
				ret.append(mul)
			j += 1
	return sum(set(ret))

n = input()
print solve(n)