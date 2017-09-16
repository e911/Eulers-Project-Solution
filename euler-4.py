a=[]
for i in range(99,1000):
	for j in range (99,1000):
		c=i*j
		if str(c) ==str(c)[::-1]:
			a.append(c)
print(a)

	
	
