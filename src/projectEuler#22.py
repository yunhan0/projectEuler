def calcScore(name):
	ret = 0
	for i in name:
		i = i.upper()
		ret += (ord(i) - 64)
	return ret


def partition(l, start, end):
	pivot = l[end-1]
	pIndex = start
	for i in range(start, end-1):
		if l[i] <= pivot:
			tmp = l[i]
			l[i] = l[pIndex]
			l[pIndex] = tmp
			pIndex +=1
	tmp = l[pIndex]
	l[pIndex] = pivot
	l[end-1] = tmp
	return pIndex

def quickSort(l, start, end):
	if start < end-1:
		p = partition(l, start, end)
		quickSort(l, start, p)
		quickSort(l, p+1, end)
	return l

N = input()
nameList = []
for i in range(N):
	name = raw_input();
	nameList.append(name)

sortedList = quickSort(nameList, 0, len(nameList))

Q = input()
for i in range(Q):
	target = raw_input()
	pos = sortedList.index(target) + 1
	print calcScore(target) * pos