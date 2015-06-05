import time

def prime(n):
	l = range(n+1)
	l[0], l[1] = False, False
	limit = int(n ** .5) + 1

	for i in range(limit):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[i * j] = False
			j += 1
	return [i for i in l if i != False]

def solve(n):
	# The pattern of the corder in the diagram:
	# Bottom right corner: n ^ 2
	# Bottom left corner: n ^ 2 - (n-1)
	# Top left corner: n ^ 2 - 2(n-1)
	# Top right corner: n ^ 2 - 3(n-1)
	# Ther number of elements on the diagonal: 2n - 1
	i = 3
	primeNumber = 0
	while True:
		total = 2 * i - 1
		for j in range(4):
			if ( i * i - j * (i - 1) ) in prime_set:
				primeNumber += 1
		if (float(primeNumber) / total * 100) < n:
			break
		i += 2
	return i

if __name__ == "__main__":
	start_time = time.time()
	prime_set = set(prime(10000));
	N = input();
	print solve(N)