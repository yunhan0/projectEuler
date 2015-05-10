def solve(num):
	n, d = 3, 2 # for the first iteration: 3/2
	for i in range(2, num+1):
		n, d = 2 * d + n, d + n
		if len(str(n)) > len(str(d)):
			print i

# Analysis:
# Expand the series as 2d + n for the numerator 
# and d+n for the denominator

N = input()
solve(N)