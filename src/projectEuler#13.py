n = input()
l = []
total = 0
for i in range(n):
	l.append(raw_input())

for i in l:
	total += int(i)

print str(total)[:10]