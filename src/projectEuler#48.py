def selfPower(n):
	ret = 0
	MOD = 10000000000
	for i in range(1, n + 1):
		ret += pow(i, i, MOD)
	ret = str(ret)[-10::]
	return int(ret)

n = input()
print selfPower(n)