import math
import time


def sum_of_divisors(num):
    sum_t = 1
    # a step to ignore iteration of even integer for odd numbers
    step = 1 if num % 2 == 0 else 2
    for i in range(2, int(math.sqrt(num)) + 1, step):
        if (num % i == 0):
            sum_t += i
            sum_t += num / i
    return sum_t
    # brute method
    # return sum([fact for fact in range(1, num) if num % fact == 0])


def amicable(n):
    a = time.time()
    amicables = set()
    for num in range(1, n + 1):
        if num in amicables:
            continue
        sum_fact = sum_of_divisors(num)
        sum_fact2 = sum_of_divisors(sum_fact)
        if num == sum_fact2 and num != sum_fact:
            amicables.add(num)
            amicables.add(sum_fact2)
    return (sum(amicables), time.time() - a)


if __name__ == "__main__":
    a = int(input("Enter a number up to which the sum of amicable numbers are needed"))
    sum_total, time_elapsed = amicable(a)
    print(sum_total, time_elapsed)
