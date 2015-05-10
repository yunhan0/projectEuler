def is_palindromic(num): 
	return str(num) == str(num)[::-1]

T = int(input())

for i in range(0, T):
	n = int(input())
	ret = 0
	root = int(n**(0.5))
	for x in xrange(100, root + 1):
		for y in xrange(root, 1000):
			tmp = x * y
			if is_palindromic(tmp) and tmp <= n:
				ret = max(tmp, ret)
			if tmp > n:
				break
	print(ret)