a = int(input('Enter a '))
b = int(input('Enter b '))


def decorator(func):
    def wrapper(first, second):
        if first == second:
            return func(first, second, operation='+')

        elif first > second:
            return func(second, first, operation='-')

        elif second > first:
            return func(first, second, operation='/')

        elif any(i < 0 for i in (first, second)):
            return func(first, second, operation='*')

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '*':
        return first * second
    elif operation == '/':
        return first / second


calc(a, b)
