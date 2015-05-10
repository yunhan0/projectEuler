def sieve(n):
	l = range(n+1)
	l[0], l[1] = False, False
	root = int(n**.5) + 1

	for i in range(2, root):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[j * i] = False
			j += 1
	return [i for i in l if i != False]

prime_list = sieve(1000)

def primeFactor(n):
	limit = len(prime_list)
	count = 0
	for i in range(limit):
		if n % prime_list[i] == 0:
			count += 1
			n = n / prime_list[i]
	return count

def distinctPrimeFactor(n, k):
	count = 0
	for i in range(1,n+1):
		if primeFactor(i) == k:
			count += 1
			for j in range(i+1,i+k):
				if primeFactor(j) == k:
					count += 1
				else:
					count = 0
					i = j + 1
					break
			if count == k:
				print i
			count = 0

n, k = raw_input().strip().split(" ")
distinctPrimeFactor(int(n),int(k))