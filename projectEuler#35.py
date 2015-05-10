def seive(n):
	l = range(n+1)
	l[0], l[1] = False, False
	root = int(n ** .5) + 1
 	for i in range(root):
 		if not l[i]:
 			continue
 		j = i
 		while j * i <= n:
 			l[j*i] = False
 			j += 1
 	return [item for item in l if item != False]

s = set(seive(1000000))

def isCircularPrime(n):
	for i in range(len(n)):
		if not int(n[i:] + n[:i]) in s:
			return False
	return True

def solve(n):
	ret = 0
	for i in xrange(2,n+1):
		if i not in s:
			continue
		if isCircularPrime(str(i)):
			ret += i
	return ret

n = input()
print solve(n) 