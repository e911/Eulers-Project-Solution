def sum_of_digits(num, power):
    return sum(map(int, str(num ** power)))


if __name__ == '__main__':
    try:
        num = int(input("Enter a number:"))
        power = int(input("Enter the power to raise the number:"))
        result = sum_of_digits(num, power)
        print(result)
    except ValueError as err:
        print("Incorrect Input: ", err)
