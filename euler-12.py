# Extra long long polling method
# Dont try this at home
#
# def triangle_list(n):
#     a=[]
#     for i in range(n):
#         c= (i+1)*(i+2)//2
#         a.append(c)
#     return a
#
# def find_factors(g):
#     c = triangle_list(g)
#     print(c)
#     factors_length=[]
#     fact_dict={}
#     for i in range(len(c)):
#         factors=[]
#         for j in range(1,c[i]+1):
#             if ((c[i])%j) == 0:
#                 factors.append(j)
#         a= len(factors)
#         fact_dict[c[i]]=a
#         factors_length.append(a)
#         for key, values in fact_dict.items():
#             if values > 500 :
#                 return (key,values)
#
# if __name__ == '__main__':
#     a=find_factors(10000000)
#     print(a)


# fast method

def num_divisors(n):
    if n % 2 == 0: n = n / 2
    divisors = 1
    count = 0
    while n % 2 == 0:
        count += 1
        n = n / 2
    divisors = divisors * (count + 1)
    p = 3
    while n != 1:
        count = 0
        while n % p == 0:
            count += 1
            n = n / p
        divisors = divisors * (count + 1)
        p += 2
    return divisors


def find_triangular_index(factor_limit):
    n = 1
    lnum, rnum = num_divisors(n), num_divisors(n + 1)
    while lnum * rnum < 500:
        n += 1
        lnum, rnum = rnum, num_divisors(n + 1)
    return n


if __name__ == '__main__':
    index = find_triangular_index(500)
    triangle = (index * (index + 1)) / 2
    print("Result %s ." % triangle)
