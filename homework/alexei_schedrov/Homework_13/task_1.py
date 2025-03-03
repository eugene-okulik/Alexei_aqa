import os
from datetime import datetime, timedelta

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
homework_path = os.path.join(file_path, 'eugene_okulik', 'hw_13', 'data.txt')


def get_dates():
    with open(homework_path, 'r') as hw_file:
        for line in hw_file.readlines():
            date_in_line = line[3:29]
            yield date_in_line


def get_date_data(index, date):
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    date = datetime.strptime(date, date_format)
    now = datetime.now()
    if index == 0:
        return f"Первая строка: {date + timedelta(days=7)}"
    elif index == 1:
        return f"Вторая строка: {date.strftime('%A')}"
    elif index == 2:
        return f"Третья строка: {now - date}"


for i, date in enumerate(get_dates()):
    result = get_date_data(i, date)
    print(result)
