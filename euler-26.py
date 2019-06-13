import time

def get_number_and_length(n):
	num = 1
	longest = 1
	for number in xrange(3,n,2):
		if number % 5 == 0:
			continue
		p = 1
		# pattern: 1/2, 1/3, 1/4....
		# logic:
		# 1/7 = .142857142 => 10/7 = 1 rem:3, 100/7 = 14 rem:3, 1000/7=142 rem:6,
		# 10000/7=1428 rem:4, 100000/7=14285 rem:5, 1000000/7=142857 rem:1, 10000000/7=1428571 rem:3 and so on...
		while (10 ** p) % number != 1:
			p += 1
		if p > longest:
			num, longest = number, p
	return num, longest

if __name__ == '__main__':
     b=time.time()
     get_result= get_number_and_length(1000)
     print(get_result, time.time()-b)
