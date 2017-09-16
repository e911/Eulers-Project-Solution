a=0
c=0
b=1
d = [0,1]
sum_even=0
while (c<4000000):
	c=a+b
	d.append(c)
	a=b
	b=c
for items in d:
	if items%2==0:
		sum_even+=items
print(sum_even)
