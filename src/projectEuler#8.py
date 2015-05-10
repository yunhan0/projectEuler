#Brute force
def greatestProduct(num, n, k):
	n = len(num)
	limit = n - k + 1
	ret = 0
	for i in range(limit):
		tmp = 1
		loc = i
		if int(num[i]) == 0: 
			tmp = 0
			continue
		for j in range(k):
			tmp *= int(num[loc])
			loc += 1
		ret = max(ret, tmp)
	print(ret)

T = int(input())

for i in range(0, T):
	n, k = raw_input().split()
	n, k = int(n), int(k)
	num = raw_input()
	greatestProduct(num, n, k)