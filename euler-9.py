
def prod_triplet_w_sum(n):
    for i in range(1,n,1):
        for j in range(1,n-i,1):
            k = n-i-j
            if i**2+j**2==k**2:
                return i*j*k,i,j,k
    return 0

if __name__ == '__main__':
	res,a,b,c=prod_triplet_w_sum(1000)
	print(res)
	print("The numbers:" ,a)
	print(b)
	print(c)

