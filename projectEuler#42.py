def getTrianglePos(i):
	if ((8 * i + 1) ** .5 - 1) % 2 == 0: 
		ret = ((8 * i + 1) ** .5 - 1) / 2
	else:
		ret = -1
	return ret

T = input()
for i in range(T):
	n = input()
	print getTrianglePos(n);