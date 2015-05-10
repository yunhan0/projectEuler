MOD = 1000000007
def spiralDigSum(n):
	n = (L-1) // 2
    return ((16*n**3 + 30*n**2 + 26*n + 3) // 3 ) % MOD

T = input()
for i in range(T):
	n = input()
	print spiralDigSum(n)