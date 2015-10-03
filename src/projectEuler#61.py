def figurateNumber( x , n ):
	if x == 3:
		return (n * n + n) / 2 # Triangle
	elif x == 4:
		return n * n # Square
	elif x == 5:
		return (3 * n * n - n) / 2 # Pentagon
	elif x == 6:
		return 2 * n * n - n
	elif x == 7:
		return (5 * n * n - 3 * n) / 2
	elif x == 8:
		return 3 * n * n - 2 * n 

def generateFigNum(l):
	dictNumbers = {}
	for i in l:
		dictNumbers[i] = []
		j = 30
		while figurateNumber(i, j) < 10000:
			if figurateNumber(i, j) < 1000:
				j += 1
				continue			
			dictNumbers[i].append(figurateNumber(i, j));
			j += 1
	return dictNumbers

# Find cicyle chain number set...

# def findNext(i):
# 	for v1 in dictNumbers.values()[i]:
# 		for v2 in dictNumbers.values()[i+1]:
# 			if v1 % 100 == v2 // 100:
				

# def solve(l):
# 	ret = []
# 	dictNumbers = generateFigNum(l)
# 	i = 0
# 	for v1 in dictNumbers.values()[i]:
# 		for v2 in dictNumbers.values()[i+1]:
# 			if v1 % 100 == v2 // 100:
# 				ret.append(v1)
# 				ret.append(v2)

# 	return ret

if __name__ == "__main__":
	T = input()
	for i in range(T):
		l = map(int, raw_input().split())
		dictNumbers = generateFigNum(l)
		print solve(l)