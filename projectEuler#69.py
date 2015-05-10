#Euler's Totient function, ϕ(n) 
#is used to determine the number of numbers less than n which are relatively prime to n. 

def sieve(n):
	l = range(0, n+1)
	l[0], l[1] = False, False
	root = int( n ** .5 ) + 1
	
	for i in range(2,root):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[j * i] = False
			j += 1
	return [item for item in l if item != False]


def totient_max(n):
	ret, i = 1, 0
	while ret * prime[i] < n:
		ret *= prime[i]
		i += 1
	return ret

if __name__ == '__main__':
	prime = sieve(100)

	T = input()
	for i in range(T):
		n = input()
		print totient_max(n)