results = [
    'результат операции: 42',
    'результат операции: 54',
    'результат работы программы: 209',
    'результат: 2'
]


def get_result(result_string):
    colon_index = result_string.index(':')
    current_result = int(result_string[colon_index + 1:].strip())
    finish_result = current_result + 10
    print(finish_result)


for result in results:
    get_result(result)
