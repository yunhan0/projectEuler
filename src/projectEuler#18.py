def solve(tri):
	while len(tri) > 1:
		t0 = tri.pop()
		t1 = tri.pop()
		tri.append( [max(t0[i], t0[i+1] ) + t for i, t in enumerate(t1)] )
	return tri[0][0]


T = input();

for i in range(T):
	N = input();
	tri = []
	for i in range(N):
		line = map(int, raw_input().split())
		tri.append(line);
	print solve(tri)