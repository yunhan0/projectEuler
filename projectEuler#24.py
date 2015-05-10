MAX_S = 13
FACTS = [1]

for i in range(1, 1+MAX_S):
	FACTS.append(FACTS[-1]*i)

# Using recursive
def getPermutation(alpha, N):
	if not alpha:
		return ''
	n = len(alpha)
	index = 0
	while FACTS[n-1] <= N:
		N -= FACTS[n-1]
		index += 1
	return alpha[index] + getPermutation( alpha[:index] + alpha[index+1:], N)
	


T = input()
target = "abcdefghijklm"
for i in range(T):
	n = long(raw_input())
	print getPermutation(list(target), n-1)