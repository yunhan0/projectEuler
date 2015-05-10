#Pythagorean Triple
def isPythagorean(n):
	ret = -1
	for a in range(1, n/2):
		b = b = n*(n - 2 * a) / ((n - a) * 2)
		if b <= 0: continue		
		b_mod = n*(n - 2 * a) % ((n - a) * 2)
		if b_mod == 0:
			c = n - a - b
			tmp =  a * b * c
		else:
			tmp = -1
		ret = max(tmp, ret)
	return ret

T = int(input())

for i in range(T):
	n = int(input())
	ans = isPythagorean(n)
	print(ans)