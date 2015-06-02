def isPalindromic(num): 
	return str(num) == str(num)[::-1]

def baseN(num,b,numerals="0123456789abcdefghijklmnopqrstuvwxyz"):
	return ((num == 0) and numerals[0]) or (baseN(num // b, b, numerals).lstrip(numerals[0]) + numerals[num % b])

def solve(n,b):
	ret = 0
	for i in range(1, n):
		if not isPalindromic(i):
			continue
		else:
			if isPalindromic(baseN(i, b)):
				ret += i 
	return ret

if __name__ == "__main__":
	N, B = map(int, raw_input().split())
	print solve(N, B)