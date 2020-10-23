import time
from itertools import permutations


# def find_millionth():
# 	list_1_to_10 ='0123456789'
# 	b=time.time()
# 	millionth = [''.join(p) for p in permutations(list_1_to_10)][999999]
# 	return (millionth , time.time()-b)

# fast version
def find_millionth():
    list_1_to_10 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = time.time()
    millionth = list(permutations(list_1_to_10))[999999]
    return (millionth, time.time() - b)


if __name__ == '__main__':
    print("The 1 millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9 ", find_millionth())
