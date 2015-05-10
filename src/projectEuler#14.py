#!/usr/bin/python
# Yunhan Li
# Date: Mar 25 2015

def collatz(n):
	cache = [0] * 101
	cache[1] = 1

	for i in range(2, n+1):
		counter, seq = 0, i
		while i!= 1 and i >= seq :
			counter += 1
			if i % 2 == 0:
				i = i / 2
			else:
				i = 3 * i + 1

		cache[seq] = counter + cache[i]	
	return cache

l = collatz(100)

ret = [0, 1]
largest = 1
for i in range(2, 101):
	ret.append(ret[i-1])
	if l[i] >= largest:
		largest = l[i]
		ret[i] = i

T = input()
for i in range(T):
	n = input()
	print ret[n]
