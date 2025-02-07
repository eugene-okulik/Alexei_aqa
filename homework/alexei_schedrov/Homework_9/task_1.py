import datetime

current_date = "Jan 15, 2023 - 12:05:33"
temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29, 31, 33, 31, 30,
                32, 30, 28, 24, 23]

python_date = datetime.datetime.strptime(current_date, '%b %d, %Y - %X')
human_month = python_date.strftime('%B')
print(human_month)
new_format_date = python_date.strftime('%d.%m.%Y, %H:%M')
print(new_format_date)

hot_days = list(filter(lambda temp: temp > 28, temperatures))
max_temp = max(hot_days)
min_temp = min(hot_days)
avg_temp = sum(hot_days) / len(hot_days)
print(f'max_temp = {max_temp} , min_temp = {min_temp} , avg_temp = {avg_temp:.2f}')
