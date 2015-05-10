def isPalindrome(n):
	return str(n) == str(n)[::-1]

D = {}

def solve(n):
	for i in range(1, n+1):
		if isPalindrome(i):
			if i in D:
				D[i] += 1
			else:
				D[i] = 1
			continue
		j = 0
		num = i			
		while j < 60:
			ret = num + int(str(num)[::-1])
			if isPalindrome(ret):
				if ret in D:
					D[ret] += 1
				else:
					D[ret] = 1
				break
			else:
				num = ret
				j += 1
	ans = max(D, key=D.get)
	print ans, D[ans]
	
N = input()
solve(N)