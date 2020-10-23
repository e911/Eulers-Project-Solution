import operator


# def collatz(n):
# 	count = {}
# 	for i in range(2,n+1):
# 		a=0
# 		d=i
# 		print(i)	
# 		while(i!=1):
# 			if i%2==0:
# 				i=i/2
# 				a+=1
# 			else:
# 				i=3*i+1
# 				a+=1
# 		count[d]=a
# 	return max(count.items(), key=operator.itemgetter(1))[0]


def collatz_optimized(n, count=1):
    while n > 1:
        count += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
    return count


def calc(n):
    max_c = [0, 0]
    for i in range(n):
        c = collatz_optimized(i)
        if c > max_c[0]:
            max_c[0] = c
            max_c[1] = i
    return max_c


if __name__ == '__main__':
    n = int(input())
    # a=collatz(n)
    b = calc(n)
    # print(a)
    print(b)
