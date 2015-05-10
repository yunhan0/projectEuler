def gcd(a, b):
	while b!= 0:
		a, b = b, a%b
	return a;

def traingle(s):
	limit = int((s/ 2) ** .5) + 1
	ret = 0
	for m in range(2, limit):
		if (s/2) % m == 0:
			if m%2 ==0:
				k = m + 1
			else:
				k = m + 2
			while k < 2 * m and k <= s / (2 * m):
				if (s/(2*m)) % k == 0 and gcd(k,m) == 1:
					ret += 1
				k += 2
	return ret

def setTraingleList(n):
	l = [0] * (n+2)
	ret = 0
	for i in xrange(12, n+1, 2):
		value = traingle(i)
		if value > ret :
			l[i] = i
			ret = value
		else:
			l[i] = l[i-1]
		l[i+1] = l[i]
	return l

MAX_S = 100000
l = setTraingleList(MAX_S)

T = input()
for i in range(T):
	n = input()
	print l[n]