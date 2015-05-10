MAX_S = 1000
FACTS = [1]
MOD = 1000000007

for i in range(1, 1+MAX_S):
  	FACTS.append((FACTS[-1]*i) % MOD)

def choose(n , k):
	return (FACTS[n]*modInv(FACTS[k]*FACTS[n-k])) % MOD

def modInv(a):
	return pow(a, MOD-2, MOD)

T = input()
for i in range(T):
	n,m = map(int, raw_input().strip().split())
	print choose(n + m, n)