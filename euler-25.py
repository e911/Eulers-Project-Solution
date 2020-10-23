import time


def fibonacci_list_last_two_numbers(n):
    last_two_numbers_in_series = [1, 1]
    if n == 1 or n == 2:
        return last_two_numbers_in_series
    else:
        for i in range(3, n + 1):
            last_two_numbers_in_series.insert(3, last_two_numbers_in_series[0] + last_two_numbers_in_series[
                1])  # insert the fin element at last of the list
            last_two_numbers_in_series.pop(
                0)  # pop out the first element in the list of the series which will be unused
    return last_two_numbers_in_series


def get_n_length_series_index(n):
    last_two_numbers_in_series = []
    fib_series_index_element = 1
    while (len(str(fibonacci_list_last_two_numbers(fib_series_index_element)[1])) != 1000):
        fib_series_index_element = fib_series_index_element + 1
        last_two_numbers_in_series = fibonacci_list_last_two_numbers(fib_series_index_element)
    return fib_series_index_element


if __name__ == '__main__':
    b = time.time()
    get_1000th_index = get_n_length_series_index(1000)
    print(get_1000th_index, time.time() - b)
