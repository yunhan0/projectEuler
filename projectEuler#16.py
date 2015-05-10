def powerSum(x):
	ret = pow(2,x)
	ret = str(ret)
	sum_ = sum(i for i in ret)
	return sum_
	
T = input()
for i in range(T):
	i = input()
	print powerSum(i)