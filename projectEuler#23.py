import time
start_time = time.time()

def seive(n):
	l = range(0, n+1)
	l[0], l[1] = False, False
	root = int(n ** .5) + 1

	for i in range(2, root):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[i * j] = False
			j += 1
	return [item for item in l if item != False]

prime_list = seive(100)

# Using sum of divisor algorithm
def sumOfDivisor(n):
	num, ret = n, 1
	limit = len(prime_list)
	for i in range(limit):
		count = 1
		while n % prime_list[i] == 0:
			count += 1
			n = n / prime_list[i]
		if count!= 1:
			ret = ret * ((prime_list[i] ** count - 1) / (prime_list[i] - 1))
	if n!= 1:
		ret = ret * ((n ** 2 - 1)/ (n - 1))
	ret = ret - num
	return ret

def abd(n):
	abdList = range(0, n+1)
	abdList[0] = False
	for i in range(1, len(abdList)):
		if i >= sumOfDivisor(i):
			abdList[i] = False
	return abdList
abdList = abd(28123)

# print("--- %s seconds ---" % (time.time() - start_time))

T = input()
for i in range(T):
	n = input()
	if n > 28123:
		print "YES"
	else:	
		ret = "NO"
		for i in range(n):
			if not abdList[i]:
				continue
			if abdList[i] > n:
				break
			if n - abdList[i] in abdList[i:n+1]:
				ret = "YES"
				break
		print ret