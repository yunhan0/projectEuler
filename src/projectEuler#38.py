def initPandigital(k):
	l = map(str, range(1,k+1))
	return set(l)

def solve(n):
	for i in range(2, n):
		m = 1
		l2 = set([])
		flag = True
		while m >= 1 and flag:
			if l2 == l1:
				print i
				break		
			ret = str(m * i)
			for c in ret:
				if c in l2:
					flag = False
					break
				else:
					l2 |= {c}
			m += 1
			
N, K = map(int, raw_input().split())
l1 = initPandigital(K)
solve(N)