buff = int(input())

for i in range(0, buff):
	n = int(input())
	f = 2 
	while f * f <= n:
		if n % f == 0:
			n = n / f
		else:
			f = f + 1
	print(n)
