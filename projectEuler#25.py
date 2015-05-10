def fibonacci(n):
	b1, b2 = 0, 1
	ret = 1
	l = [0] * (n+1)
	for i in range(2, n+1):
		ret = b1 + b2
		length = len(str(ret))
		if l[length] == 0:
			l[length] = i
		b1 = b2
		b2 = ret
	return l

l = fibonacci(24000)

T = input()
for i in range(T):
	n = input()
	print l[n]