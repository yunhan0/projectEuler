buff = int(input())
for i in range(0, buff) :
	x = int(input());
	n = (x-1) / 3;
	sum = n * 3 + 3*n*(n-1) /2; 
	n = (x-1) / 5;
	sum += n * 5 + 5*n*(n-1) /2;
	n = (x-1) / 15;
	sum -= n * 15 + 15*n*(n-1) /2;
	print sum