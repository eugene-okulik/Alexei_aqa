import sys

sys.set_int_max_str_digits(10 ** 6)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def get_fibonacci_number(n):
    fib_gen = fibonacci()
    count = 1
    for value in fib_gen:
        if count == n:
            return value
        count += 1


numbers_list = [5, 200, 1000, 100000]

for number in numbers_list:
    print(f"{number}-е число Фибоначчи : {get_fibonacci_number(number)}")
