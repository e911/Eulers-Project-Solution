def square_sum(a):
    sum_num = a * (a + 1) // 2;
    return sum_num ** 2


def sum_square(a):
    square_sum = a * (a + 1) * (2 * a + 1) // 6
    return (square_sum)


print(square_sum(100) - sum_square(100))
