first_result = 'результат операции: 42'
second_result = 'результат операции: 514'
program_result = 'результат работы программы: 9'
# Находим индекс двоеточия
first_index = first_result.index(':')
second_index = second_result.index(':')
third_index = program_result.index(':')
# Берем часть строки после двоеточия , обрезаем пробел и преобразуем в целое число
first_number = int(first_result[first_index + 1:].strip())
second_number = int(second_result[second_index + 1:].strip())
third_number = int(program_result[third_index + 1:].strip())
# Увеличиваем на 10 каждое число
print(first_number + 10)
print(second_number + 10)
print(third_number + 10)
