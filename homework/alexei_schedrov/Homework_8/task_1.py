import random

salary = int(input("Введите зарплату : $ "))
bonus = random.choice([True, False])
if bonus:
    bonus_amount = random.randint(1000, 10000)
    final_salary = salary + bonus_amount
else:
    final_salary = salary
print(f"{salary}, {bonus} - '${final_salary}'")
