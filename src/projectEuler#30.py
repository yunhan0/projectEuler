def isDigitPower(n, e):
	ret, number = 0, n
	while number > 0:
		remain = number % 10
		number /= 10
		ret += pow(remain, e)
	if ret == n:
		return True
	else:
		return False

def solve(n):
	limit = 9 ** n * (n-1)
	ret = 0
	for i in range(100, limit):
		if isDigitPower(i, n):
			ret += i
	return ret

N = input()
print solve(N)