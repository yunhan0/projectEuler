def solve(n, k):
	cube = {}
	for i in range(1, n):
		j = pow(i, 3)
		digits = "".join(sorted(str(j)))
		if digits in cube:
			cube[digits].append(j)
		else:
			cube[digits] = [j]

	ret = [ min(i) for i in cube.values() if len(i) == k]
	ret = sorted(ret)
	if ret != []:
		for i in ret:
			print i

n, k = map(int, raw_input().split())
solve(n, k)