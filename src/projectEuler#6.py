def squareOfSum(n):
	sum = ((n+1)*n)/2
	return sum ** 2

T = int(input())

for i in range(0, T):
	n = int(input())
	sqr , sums  = 0, squareOfSum(n) 
	while n >= 1:
		sqr += n * n
		n -= 1
	ret = sums - sqr
	print(ret)