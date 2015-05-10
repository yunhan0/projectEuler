def solve(n):
	ret = 1
	for i in range(1, n):
		for j in range(1, n):
			x = map(long, list(str(pow(i, j))))
			ret = max(ret, sum(x))
	return ret

n = input()
print solve(n)