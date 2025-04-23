import mysql.connector as mysql
import csv
import os
import dotenv

dotenv.load_dotenv()

base_path = os.path.dirname(__file__)
file_path = os.path.dirname(os.path.dirname(base_path))
homework_file = os.path.join(file_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')

db = mysql.connect(
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSW'),
    host=os.getenv('DB_HOST'),
    port=os.getenv('DB_PORT'),
    database=os.getenv('DB_NAME')
)
cursor = db.cursor(dictionary=True)


def get_db_data():
    query = """
    SELECT
    s.name,
    s.second_name,
    g.title AS group_title,
    b.title AS book_title,
    sub.title AS subject_title,
    l.title AS lesson_title,
    m.value AS mark_value
FROM
    students s
JOIN
    `groups` g ON s.group_id = g.id
LEFT JOIN
    books b ON b.taken_by_student_id = s.id
LEFT JOIN
    marks m ON s.id = m.student_id
LEFT JOIN
    lessons l ON m.lesson_id = l.id
LEFT JOIN
    subjets sub ON l.subject_id = sub.id
    """
    cursor.execute(query)
    return cursor.fetchall()


def read_file_data():
    with open(homework_file, newline='') as csv_file:
        file_data = csv.reader(csv_file)
        headers = next(file_data)
        return [dict(zip(headers, row)) for row in file_data]


for student_data in read_file_data():
    if student_data not in get_db_data():
        print(f"Этих данных нет в БД : {student_data}")

db.close()
