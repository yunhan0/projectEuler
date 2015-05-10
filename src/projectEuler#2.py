buff = int(input())
for i in range(0, buff):
	n = int(input())
	a = 1
	b = 2
	total = 0
	while b <= n:
		if b % 2 == 0 :
			total += b
		a, b = b, a+b
	print(total)
