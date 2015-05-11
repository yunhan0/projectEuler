def solve(n):
	i = 1
	while True: 
		ret = pow(i, n)
		if len(str(ret)) > n:
			break
		if len(str(ret)) == n:
			print ret
		i += 1

N = input()
solve(N)