def numList(i):
	l = []
	while True:
		l.append(i % 10)
		i = i / 10
		if i == 0:
			break
	l.sort()
	return l

def permutedMultiple(n, k):
	for i in range(1, n + 1):
		l1 = numList(i)
		foo = [i]
		for j in range (2, k+1):
			ret = i * j
			if l1 != numList(ret):
				break
			foo.append(ret)
			if j == k:
				print " ".join(map(str, foo))

N, K = map(int, raw_input().split())
permutedMultiple(N, K)