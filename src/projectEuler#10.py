def sieve(n):
	l = range(0, n+1)
	l[0], l[1] = False, False
	root = int(n ** .5) + 1

	for i in range(2, root):
		if not l[i]:
			continue
		j = i
		while i * j <= n:
			l[i * j] = False
			j += 1
	return l

l = sieve(1000000)

ret = [0, 0]
for i in range(2, 1000001):
	ret.append(ret[i - 1])
	if l[i]:
		ret[i] += i

T = int(input())

for i in range(T):
	n = int(input())
	print ret[n]