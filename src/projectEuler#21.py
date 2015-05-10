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
			j+=1
	return [item for item in l if item != False]

prime_list = sieve(100)

def sumOfDivisor(n):
	num , ret = n, 1
	limit = len(prime_list)
	for i in range(limit):
		count = 1
		while n % prime_list[i] == 0:
			count += 1
			n = n / prime_list[i]
		if count != 1:
			ret = ret * ((prime_list[i] ** count - 1 ) / (prime_list[i] - 1))
	if n!= 1:
		ret = ret * ((n ** 2 - 1 ) / (n - 1))
	ret = ret - num
	return ret

def amicableNum(n):
	amicable_list = [False] * n
	for i in range(2, n+1):
		a1 = sumOfDivisor(i)
		if a1 <= i:
			continue
		a2 = sumOfDivisor(a1)
		if a2 == i:
			amicable_list[a1] = True
			amicable_list[i] = True
	return amicable_list

amicable_list = amicableNum(100000)

T = input()
for i in range(T):
	n = input()
	ret = 0
	for j in range(n):
		if not amicable_list[j]:
			continue
		else:
			ret += j
	print ret