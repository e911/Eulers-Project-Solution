from functools import reduce
b=[]
a=20
for i in range(2,a):
	if all(i%a!=0 for a in range(2,i//2)):
		b.append(i)
print(b)
z= reduce(lambda x, y: x*y,b)

print(z)