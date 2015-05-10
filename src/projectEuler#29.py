def distinctPower(n):
	s = set()
	for i in range(2, n+1):
		for j in range(2, n+1):
			ret = pow(i, j)
			s.add(ret)
	return len(s)

n = input()
print distinctPower(n)