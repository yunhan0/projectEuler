def triangleVal(i):
	return i * (i + 1) / 2

def sievePrime(n):
	l = range(0, n)
	l[0], l[1] = False, False
	root = int(n ** .5) + 1

	for i in range(2, root):
		if not l[i]:
			continue
		j = i
		while i * j < n:
			l[i * j] = False
			j += 1
	return [item for item in l if item != False]

prime_list = sievePrime(42)

def primeFactorize(n):
	limit = len(prime_list)
	divisors = 1
	for i in range(limit):
		count = 0
		while n % prime_list[i] == 0:
			count += 1
			n = n / prime_list[i]
		divisors = divisors * (count + 1)
	return divisors

T = int(input())
for i in range(T):
	n = int(input())
	j = 1
	while j > 0:
		num = triangleVal(j)
		ret = primeFactorize(num)
		if ret > n:
			print num
			break
		j += 1
