def seive(n):
	l = range(n+1)
	l[0], l[1] = False, False
	limit = int(n ** .5) + 1
	for i in range(1,limit):
		if not l[i]:
			continue
		j = i
		while j * i <= n:
			l[j * i] = False
			j += 1
	return [i for i in l if i != False]

l = seive(3000000)
s = set(l)

def trunc(i):
	num = str(i)
	j = 1
	while j < len(num):
		if int(num[j:]) in s and int(num[:j]) in s:
			j += 1
		else:
			return 0
	return i


def solve(n):
	ret = 0
	i = 4
	while l[i] < n:
		if l[i] == trunc(l[i]):
			ret += l[i]
		i += 1
	return ret

N = input()
print solve(N)