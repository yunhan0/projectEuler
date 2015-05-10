MAX_S = 1000
FACTS = [1, 1]

for i in range(2, 1 + MAX_S):
	FACTS.append(FACTS[-1]*i)

FACTS = [str(i) for i in FACTS]

def sumOfDigits(s):
	return sum(int(i) for i in s)

T = input()
for i in range(T):
	n = input()
	print sumOfDigits(FACTS[n])