def gcd(a, b):
	while b!= 0:
		a, b = b, a%b
	return a;

def lcm(a, b):
	return a * b // gcd(a, b)

T = int(input())

for i in range(0, T):
	n = int(input())
	ret = ( n > 1 ) and n - 1 or 1
	while n >= 1:
		ret = lcm(n, ret )
		n -= 1
	print(ret)

	