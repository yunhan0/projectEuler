FACT = [1]
for i in range(1,10):
	FACT.append((FACT[-1] * i))
print FACT

def digitFact(n):
	ret = 0
	while n > 0:
		ret += FACT[n % 10]
		n = n / 10
	return ret

def solve(n):
	ret = 0
	for i in range(10, n):
		if digitFact(i) % i == 0:
			ret += i
		else:
			continue
	return ret

N = input()
print solve(N)