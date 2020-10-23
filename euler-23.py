import math
import time
from functools import reduce


def is_abundant(n):
    sum_of_divisors = 0
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            sum_of_divisors += i
        else:
            pass
    return (True if sum_of_divisors > n else False)


def list_of_abundant_numbers(n=28123):
    list_num = []
    for i in range(n):
        if is_abundant(i):
            list_num.append(i)
        else:
            pass
    return list_num


def list_of_sum_of_every_two_abundant_numbers(list_of_abundant_numbers):
    list_sum = []
    for each in list_of_abundant_numbers:
        for each_n in list_of_abundant_numbers:
            list_sum.append(each + each_n)
    return list_sum


def list_of_non_abundant_numbers_till_n(list_of_sum_of_every_two_abundant_numbers, n=28123):
    list_all = list(range(n))
    # list_of_non_abundant_numbers = [x for x in list_all if x not in list_of_sum_of_every_two_abundant_numbers]
    list_of_non_abundant_numbers = list(set(list_all).difference(set(list_of_sum_of_every_two_abundant_numbers)))
    return list_of_non_abundant_numbers


# def list_of_non_abundant_numbers_till_n(list_of_abundant_numbers,n=28123):
# 	list_all = list(range(n))
# 	for each in list_of_abundant_numbers:
# 		for each_n in list_of_abundant_numbers:		
# 			if (each+each_n) in list_all:
# 				list_all.remove(each+each_n)
# 	return list_all


def sum_of_elements_of_list(n):
    return reduce(lambda x, y: x + y, n)


if __name__ == '__main__':
    start = time.time()
    list_of_abundant_numbers = list_of_abundant_numbers()

    list_of_sum_of_every_two_abundant_numbers = list_of_sum_of_every_two_abundant_numbers(list_of_abundant_numbers)
    list_of_non_abundant_numbers_till_n = list_of_non_abundant_numbers_till_n(list_of_sum_of_every_two_abundant_numbers)
    result = sum_of_elements_of_list(list_of_non_abundant_numbers_till_n)

    # list_of_sum_non_abundant_numbers = list_of_non_abundant_numbers_till_n(list_of_abundant_numbers)
    # result =  sum_of_elements_of_list(list_of_sum_non_abundant_numbers)

    elapsed = (time.time() - start)
    print("%s found in %s seconds" % (result, elapsed))
