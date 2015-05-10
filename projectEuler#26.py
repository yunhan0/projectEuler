def getCycleLength(n):
	rlist = [0] * n
	remain = 1
	pos = 1
	ret = 0
	while remain!= 0:
		remain = (remain * 10) % n
		if rlist[remain] == 0:
			rlist[remain] = pos
			pos += 1
		else:
			ret = pos - rlist[remain]
			break
	return ret

def setLongCycleTable(n):
	l = [0, 0]
	value = 0
	for i in range(2, n+1):
		length = getCycleLength(i)
		if length > value:
			l.append(i)
			value = length
		else:
			l.append(l[-1])
	return l
CycleTable = setLongCycleTable(10000)	
print CycleTable
T = input()
for i in range(T):
	n = input()
	print CycleTable[n-1]