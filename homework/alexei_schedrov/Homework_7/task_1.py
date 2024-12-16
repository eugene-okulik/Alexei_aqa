x = 7
answer = int(input("Угадайте число "))
while True:
    if x != answer:
        answer = int(input("попробуйте снова "))
        continue
    print('Поздравляю! Вы угадали!')
    break
