def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def sum_of_digits(number):
    fact = factorial(number)
    return sum(map(int, str(fact)))


if __name__ == "__main__":
    num = int(input("Enter a number"))
    result = sum_of_digits(num)
    print(result)
